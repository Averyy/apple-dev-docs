# AVAudioEngine

**Framework**: AVFAudio  
**Kind**: class

An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioEngine
```

## Mentions

- [Routing audio to specific devices in multidevice sessions](routing-audio-to-specific-devices-in-multidevice-sessions.md)

#### Overview

An audio engine object contains a group of [`AVAudioNode`](avaudionode.md) instances that you attach to form an audio processing chain.

![A flow diagram that shows an app using an audio engine in a real time context. The audio flows from the source file in the app to a player node, a mixer node, and an output node before reaching the device’s speaker or connected headphones.](https://docs-assets.developer.apple.com/published/7c3d9ef3dfa5c67520afa13402f65a9d/media-3901205%402x.png)

You can connect, disconnect, and remove audio nodes during runtime with minor limitations. Removing an audio node that has differing channel counts, or that’s a mixer, can break the graph. Reconnect audio nodes only when they’re upstream of a mixer.

By default, Audio Engine renders to a connected audio device in real time. You can configure the engine to operate in manual rendering mode when you need to render at, or faster than, real time. In that mode, the engine disconnects from audio devices and your app drives the rendering.

##### Create an Engine for Audio File Playback

To play an audio file, you create an [`AVAudioFile`](avaudiofile.md) with a file that’s open for reading. Create an audio engine object and an [`AVAudioPlayerNode`](avaudioplayernode.md) instance, and then attach the player node to the engine. Next, connect the player node to the audio engine’s output node. The engine performs audio output through an output node, which is a singleton that the engine creates the first time you access it.

```swift
let audioFile = /* An AVAudioFile instance that points to file that's open for reading. */
let audioEngine = AVAudioEngine()
let playerNode = AVAudioPlayerNode()

// Attach the player node to the audio engine.
audioEngine.attach(playerNode)

// Connect the player node to the output node.
audioEngine.connect(playerNode, 
                    to: audioEngine.outputNode, 
                    format: audioFile.processingFormat)
```

Then schedule the audio file for full playback. The callback notifies your app when playback completes.

```swift
playerNode.scheduleFile(audioFile, 
                        at: nil, 
                        completionCallbackType: .dataPlayedBack) { _ in
    /* Handle any work that's necessary after playback. */
}
```

Before you play the audio, start the engine.

```swift
do {
    try audioEngine.start()
    playerNode.play()
} catch {
    /* Handle the error. */
}
```

When you’re done, stop the player and the engine.

```swift
playerNode.stop()
audioEngine.stop()
```

## Topics

### Creating an Audio Engine
- [init()](avaudioengine/init.md)
  Creates an audio engine instance for rendering in real time.
### Attaching and Detaching Audio Nodes
- [func attach(AVAudioNode)](avaudioengine/attach(_:).md)
  Attaches an audio node to the audio engine.
- [func detach(AVAudioNode)](avaudioengine/detach(_:).md)
  Detaches an audio node from the audio engine.
- [var attachedNodes: Set<AVAudioNode>](avaudioengine/attachednodes.md)
  A read-only set that contains the nodes you attach to the audio engine.
### Getting the Input, Output, and Main Mixer Nodes
- [var inputNode: AVAudioInputNode](avaudioengine/inputnode.md)
  The audio engine’s singleton input audio node.
- [var outputNode: AVAudioOutputNode](avaudioengine/outputnode.md)
  The audio engine’s singleton output audio node.
- [var mainMixerNode: AVAudioMixerNode](avaudioengine/mainmixernode.md)
  The audio engine’s optional singleton main mixer node.
### Connecting and Disconnecting Audio Nodes
- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](avaudioengine/connect(_:to:format:).md)
  Establishes a connection between two nodes.
- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:tobus:format:).md)
  Establishes a connection between two nodes, specifying the input and output busses.
- [func disconnectNodeInput(AVAudioNode)](avaudioengine/disconnectnodeinput(_:).md)
  Removes all input connections of the node.
- [func disconnectNodeInput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeinput(_:bus:).md)
  Removes the input connection of a node on the specified bus.
- [func disconnectNodeOutput(AVAudioNode)](avaudioengine/disconnectnodeoutput(_:).md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeoutput(_:bus:).md)
  Removes the output connection of a node on the specified bus.
### Managing MIDI Nodes
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistblock:)-73cd1.md)
  Establishes a MIDI connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, eventListBlock: AUMIDIEventListBlock?)](avaudioengine/connectmidi(_:to:format:eventlistblock:)-7qtd5.md)
  Establishes a MIDI connection between a source node and multiple destination nodes.
- [func disconnectMIDI(AVAudioNode, from: AVAudioNode)](avaudioengine/disconnectmidi(_:from:)-1kssy.md)
  Removes a MIDI connection between two nodes.
- [func disconnectMIDI(AVAudioNode, from: [AVAudioNode])](avaudioengine/disconnectmidi(_:from:)-7oaab.md)
  Removes a MIDI connection between one source node and multiple destination nodes.
- [func disconnectMIDIInput(AVAudioNode)](avaudioengine/disconnectmidiinput(_:).md)
  Disconnects all input MIDI connections from a node.
- [func disconnectMIDIOutput(AVAudioNode)](avaudioengine/disconnectmidioutput(_:).md)
  Disconnects all output MIDI connections from a node.
- [func connectMIDI(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](avaudioengine/connectmidi(_:to:format:block:)-3bc13.md)
  Establishes a MIDI-only connection between two nodes.
- [func connectMIDI(AVAudioNode, to: [AVAudioNode], format: AVAudioFormat?, block: AUMIDIOutputEventBlock?)](avaudioengine/connectmidi(_:to:format:block:)-666bc.md)
  Establishes a MIDI-only connection between a source node and multiple destination nodes.
### Playing Audio
- [func prepare()](avaudioengine/prepare.md)
  Prepares the audio engine for starting.
- [func start() throws](avaudioengine/start.md)
  Starts the audio engine.
- [var isRunning: Bool](avaudioengine/isrunning.md)
  A Boolean value that indicates whether the audio engine is running.
- [func pause()](avaudioengine/pause.md)
  Pauses the audio engine.
- [func stop()](avaudioengine/stop.md)
  Stops the audio engine and releases any previously prepared resources.
- [func reset()](avaudioengine/reset.md)
  Resets all audio nodes in the audio engine.
- [var musicSequence: MusicSequence?](avaudioengine/musicsequence.md)
  The music sequence instance that you attach to the audio engine, if any.
### Manually Rendering an Audio Engine
- [func enableManualRenderingMode(AVAudioEngineManualRenderingMode, format: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws](avaudioengine/enablemanualrenderingmode(_:format:maximumframecount:).md)
  Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.
- [func disableManualRenderingMode()](avaudioengine/disablemanualrenderingmode.md)
  Sets the engine to render to or from an audio device.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](avaudioengine/renderoffline(_:to:).md)
  Makes a render call to the engine operating in the offline manual rendering mode.
### Getting Manual Rendering Properties
- [typealias AVAudioEngineManualRenderingBlock](avaudioenginemanualrenderingblock.md)
  The type that represents a block that renders the engine when operating in manual rendering mode.
- [var manualRenderingBlock: AVAudioEngineManualRenderingBlock](avaudioengine/manualrenderingblock.md)
  The block that renders the engine when operating in manual rendering mode.
- [var manualRenderingFormat: AVAudioFormat](avaudioengine/manualrenderingformat.md)
  The render format of the engine in manual rendering mode.
- [var manualRenderingMaximumFrameCount: AVAudioFrameCount](avaudioengine/manualrenderingmaximumframecount.md)
  The maximum number of PCM sample frames the engine produces in any single render call in manual rendering mode.
- [var manualRenderingMode: AVAudioEngineManualRenderingMode](avaudioengine/manualrenderingmode.md)
  The manual rendering mode configured on the engine.
- [var manualRenderingSampleTime: AVAudioFramePosition](avaudioengine/manualrenderingsampletime.md)
  An indication of where the engine is on its render timeline in manual rendering mode.
- [var isAutoShutdownEnabled: Bool](avaudioengine/isautoshutdownenabled.md)
  A Boolean value that indicates whether autoshutdown is in an enabled state.
- [var isInManualRenderingMode: Bool](avaudioengine/isinmanualrenderingmode.md)
  A Boolean value that indicates whether the engine is operating in manual rendering mode.
### Using Connection Points
- [class AVAudioConnectionPoint](avaudioconnectionpoint.md)
  A representation of either a source or destination connection point in the audio engine.
- [func connect(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:format:).md)
  Establishes a connection between a source node and multiple destination nodes.
- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](avaudioengine/inputconnectionpoint(for:inputbus:).md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](avaudioengine/outputconnectionpoints(for:outputbus:).md)
  Returns connection information about a node’s output bus.
### Constants
- [enum AVAudioEngineManualRenderingError](avaudioenginemanualrenderingerror.md)
  Constants that describe error codes that the framework returns from manual rendering mode methods.
- [enum AVAudioEngineManualRenderingMode](avaudioenginemanualrenderingmode.md)
  The two modes for manual rendering.
- [enum AVAudioEngineManualRenderingStatus](avaudioenginemanualrenderingstatus.md)
  Status codes that return from the render call to the engine operating in manual rendering mode.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine)*