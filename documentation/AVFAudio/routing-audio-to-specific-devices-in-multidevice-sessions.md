# Routing audio to specific devices in multidevice sessions

**Framework**: AVFAudio

Map audio channels to specific devices in multiroute sessions for recording and playback.

#### Overview

When working with multiple audio devices simultaneously, such as recording from multiple microphones or routing playback to different speakers, you need precise control over which audio reaches which device.

[`Core Audio`](https://developer.apple.com/documentation/CoreAudio) provides channel mapping to bind specific audio channels to targeted devices. Use the input and output nodes from [`AVAudioEngine`](avaudioengine.md) for position-based routing with global channel indices, [`Audio Queue Services`](https://developer.apple.com/documentation/AudioToolbox/audio-queue-services) for device-based routing using device identifiers, or [`AVAudioPlayer`](avaudioplayer.md) and [`AVAudioRecorder`](avaudiorecorder.md) for high-level routing with audio session channel descriptions.

#### Route Audio Outputs Using Audio Engines Output Node

Use [`Audio Unit`](https://developer.apple.com/documentation/AudioUnit) channel maps to route playback audio to specific devices by mapping to global channel positions. A channel map is an array where the index represents the destination channel and the value specifies which source channel to route to that destination. Use `-1` to specify silence for unused channels.

In multidevice configurations, [`Core Audio`](https://developer.apple.com/documentation/CoreAudio) flattens all device channels into a sequential global channel space. When multiple audio devices are active, Core Audio assigns channels sequentially based on port order. For example, with AirPods (2 channels) and built-in speaker (2 channels) connected:

```swift
Device 1 (AirPods): 2 channels > Global positions [0, 1]
Device 2 (Built-in): 2 channels > Global positions [2, 3]
Result: Global channel array [0, 1, 2, 3]
```

To route a stereo audio file to the built-in speaker at channels 2 and 3, create a channel map sized to match the total output channels:

```swift
var channelMap: [Int32] = [-1, -1, 0, 1]
// channelMap[0] = -1: AirPods left is silent.
// channelMap[1] = -1: AirPods right is silent.
// channelMap[2] = 0: Built-in left plays the file's left channel.
// channelMap[3] = 1: Built-in right plays the file's right channel.
```

Because port order can vary and channel counts differ between devices, first discover the actual port-to-channel mapping via [`currentRoute`](avaudiosession/currentroute.md). Calculate channel indices dynamically based on the current audio route configuration:

```swift
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

let currentRoute = audioSession.currentRoute
var outputChannelOffset: UInt32 = 0

for (portIndex, outputPort) in currentRoute.outputs.enumerated() {
    guard let channels = outputPort.channels else { continue }

    // The `outputChannelOffset` is the starting global channel index 
    // for this device.

    // Increase the `outputChannelOffset` by the number of 
    // channels in this port.
    outputChannelOffset += UInt32(channels.count)
}
```

This iterates through output ports, calculating their position in the global flattened channel array. Use these calculated indices to target specific devices in your channel mapping.

After discovering channel positions, configure the [`Audio Unit`](https://developer.apple.com/documentation/AudioUnit) with a channel map. This example routes a stereo audio file to the built-in speaker, assuming it occupies channels 2 and 3 in the global channel space:

```swift
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

// Configure audio IO.
let engine = AVAudioEngine()
let player = AVAudioPlayerNode()

engine.attach(player)
engine.connect(player, to: engine.mainMixerNode, format: nil)

guard let outputAudioUnit = engine.outputNode.audioUnit else {
    fatalError("Failed to get output AudioUnit")
}

// Get the total output channels from the 
// audio session.
let totalOutputChannels = audioSession.maximumOutputNumberOfChannels

// Create the channel map: 
// Silence all channels except target device.
var channelMap = Array<Int32>(repeating: -1, count: totalOutputChannels)

// Route stereo audio to built-in speaker at channels 2 and 3.
channelMap[2] = 0  // Route stream channel 0 (left) to output channel 2.
channelMap[3] = 1  // Route stream channel 1 (right) to output channel 3.

// Apply the channel map to `AudioUnit`.
let result = AudioUnitSetProperty(
    outputAudioUnit,
    kAudioOutputUnitProperty_ChannelMap,
    kAudioUnitScope_Output,
    0,
    channelMap,
    UInt32(channelMap.count * MemoryLayout<Int32>.size)
)

guard result == noErr else {
    fatalError("Failed to set channel map: \(result)")
}

// Start the audio engine and play audio.
try? engine.start()

guard let audioFileURL = Bundle.main.url(forResource: "sample", withExtension: "mp3"),
      let audioFile = try? AVAudioFile(forReading: audioFileURL) else {
    fatalError("Failed to load audio file")
}

player.scheduleFile(audioFile, at: nil)
player.play()
```

> **Note**: The channel map array size must match the total number of output channels available. Each element specifies the source stream channel for that output position, or `-1` for silence.

#### Route Audio Inputs Using Audio Engines Input Node

When recording from multiple input devices, channel map semantics differ from playback. The channel map array size must match your desired recording channel count (not the total hardware channel count), and each array element specifies which hardware channel to pull from.

In multidevice input configurations, similar to output, hardware channels are available sequentially. For example, with a device’s stereo built-in microphone (2 channels: front and back) and AirPods microphone (1 channel):

```swift
Device 1 (Built-in Mic): 2 channels > Hardware channels [0, 1] (front, back)
Device 2 (AirPods Mic): 1 channel > Hardware channel [2]
Result: Hardware channel array [0, 1, 2]
```

To record a two-channel file capturing audio from the device’s built-in front mic (channel 0) and AirPods (channel 2), set the input client format to 2 channels, then create a channel map sized to match the desired recording channel count:

```swift
var channelMap: [Int32] = [0, 2]
// channelMap[0] = 0: File channel 0 records from Built-in front mic (hardware channel 0).
// channelMap[1] = 2: File channel 1 records from AirPods mic (hardware channel 2).
```

Discover the available input channels:

```swift
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

let currentRoute = audioSession.currentRoute

for (portIndex, inputPort) in currentRoute.inputs.enumerated() {
    guard let channels = inputPort.channels else { continue }

    print("Port \(portIndex): \(inputPort.portName)")
    for (channelIndex, channel) in channels.enumerated() {
        print("  Hardware channel \(channelIndex): \(channel.channelName)")
    }
}
```

Configure the input channel map to select specific hardware channels for recording. This example records a two-channel file from hardware channels 0 and 2:

```swift
// Configure audio IO.
let engine = AVAudioEngine()
let inputNode = engine.inputNode

// Get the hardware input format to match the sample rate.
let hwFormat = inputNode.inputFormat(forBus: 0)

// Create the recording format with the desired channel count
// and hardware sample rate.
let recordingFormat = AVAudioFormat(
    standardFormatWithSampleRate: hwFormat.sampleRate,
    channels: 2
)!

// Configure the channel map using the underlying `AudioUnit`.
guard let inputAudioUnit = inputNode.audioUnit else {
    fatalError("Failed to get input AudioUnit")
}

var channelMap: [Int32] = [
    0, // File channel 0 < Hardware channel 0.
    2 // File channel 1 < Hardware channel 2.
]

let result = AudioUnitSetProperty(
    inputAudioUnit,
    kAudioOutputUnitProperty_ChannelMap,
    kAudioUnitScope_Input,
    1,
    channelMap,
    UInt32(channelMap.count * MemoryLayout<Int32>.size)
)

guard result == noErr else {
    fatalError("Failed to set input channel map: \(result)")
}

// Install tap with recording format to start capturing audio.
inputNode.installTap(onBus: 0, bufferSize: 4096, format: recordingFormat) { buffer, time in
    // Process the recorded audio buffer here.
    // Example: Write to file, analyze audio, and so on.
}

// Start the engine.
try engine.start()
```

> **Note**: When using AVAudioEngine, set the client format by passing your desired format to `installTapOnBus`. The format’s channel count should match your channel map size, and the sample rate should match the hardware input format to avoid runtime errors.

#### Route Audio with Audio Queue Channel Assignments

Use [`Audio Queue Services`](https://developer.apple.com/documentation/AudioToolbox/audio-queue-services) channel assignments to route audio to specific device channels by device UID rather than global channel position. This approach provides direct device targeting without needing to calculate global channel indices.

Set the [`kAudioQueueProperty_ChannelAssignments`](https://developer.apple.com/documentation/AudioToolbox/kAudioQueueProperty_ChannelAssignments) property with an [`AudioQueueChannelAssignment`](https://developer.apple.com/documentation/AudioToolbox/AudioQueueChannelAssignment) structure specifying the target device UID and channel number:

```swift
// Get the device UID from `AVAudioSession`.
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

let outputPort = audioSession.currentRoute.outputs.first!

// Create the channel assignment for device channel 0.
var channelAssignment = AudioQueueChannelAssignment(
    mDeviceUID: outputPort.uid as CFString,
    mChannelNumber: 1  // 1-based indexing.
)

// Apply the channel assignments to `AudioQueue`
AudioQueueSetProperty(
    audioQueue,
    kAudioQueueProperty_ChannelAssignments,
    &channelAssignment,
    UInt32(MemoryLayout<AudioQueueChannelAssignment>.size)
)
```

#### Route High Level Audio an Audio Player or Recorder

[`AVAudioPlayer`](avaudioplayer.md) and [`AVAudioRecorder`](avaudiorecorder.md) provide a high-level approach using the audio player’s [`channelAssignments`](avaudioplayer/channelassignments.md), or the audio recorder’s [`channelAssignments`](avaudiorecorder/channelassignments.md) property with [`AVAudioSessionChannelDescription`](avaudiosessionchanneldescription.md) objects directly from the audio session.

> **Note**: For [`AVAudioPlayer`](avaudioplayer.md), the `channelAssignments` array count should match the audio format’s channel count.

For output [`AVAudioPlayer`](avaudioplayer.md):

```swift
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

let outputPort = audioSession.currentRoute.outputs.first!
let channelDescription = outputPort.channels!.first!

let player = try AVAudioPlayer(contentsOf: audioFileURL)
player.channelAssignments = [channelDescription]
player.play()
```

For input with [`AVAudioRecorder`](avaudiorecorder.md):

```swift
let audioSession = AVAudioSession.sharedInstance()

// Configure and activate the audio session for multiroute setup.

let inputPort = audioSession.currentRoute.inputs.first!
let channelDescription = inputPort.channels!.first!

let recorder = try AVAudioRecorder(url: outputURL, settings: settings)
recorder.channelAssignments = [channelDescription]
recorder.record()
```

## See Also

- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md)
  Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioSession](avaudiosession.md)
  An object that communicates to the system how you intend to use audio in your app.
- [class AVAudioApplication](avaudioapplication.md)
  An object that manages one or more audio sessions that belong to an app.
- [class AVAudioRoutingArbiter](avaudioroutingarbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/routing-audio-to-specific-devices-in-multidevice-sessions)*