# Matching audio using the built-in microphone

**Framework**: ShazamKit

Use the audio stream from the microphone as the source for a ShazamKit session.

#### Overview

Use an audio engine with a mixer node to connect to the microphone and convert the audio format into one that’s compatible with ShazamKit. You’ll also need to add a description of the intended use of the microphone.

##### Add a Microphone Use Description

The microphone is a protected resource and requires permission from the user. Your app must provide a description of the intended use by adding a `Privacy - Microphone Usage Description` key to App Info. For more information on accessing protected resources, see [`Requesting access to protected resources`](https://developer.apple.com/documentation/UIKit/requesting-access-to-protected-resources).

##### Configure an Audio Mixer and Install a Tap

Access the microphone using [`AVAudioEngine`](https://developer.apple.com/documentation/AVFAudio/AVAudioEngine) and an [`AVAudioMixerNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioMixerNode) to convert the sound into one that’s compatible with ShazamKit.

Start by adding properties to your matcher class for the audio engine and mixer node. Then add a property for the active ShazamKit session.

```swift
let audioEngine = AVAudioEngine()
let mixerNode = AVAudioMixerNode()

// The session for the active ShazamKit match request.
let session: SHSession?
```

Add a function that appends an audio buffer to the buffer used for matching. The audio engine calls this function when new audio is available.

```swift
func addAudio(buffer: AVAudioPCMBuffer, audioTime: AVAudioTime) {
    // Add the audio to the current match request.
    session?.matchStreamingBuffer(buffer, at: audioTime)
}
```

Next, add a method that configures the audio engine and mixer, and installs the tap that calls your add audio function. A tap provides access to the input of the audio engine. Call this function from the initialization code for your object because you only need to set up the engine once.

```swift
func configureAudioEngine() {
    // Get the native audio format of the engine's input bus.
    let inputFormat = audioEngine.inputNode.inputFormat(forBus: 0)
    
    // Set an output format compatible with ShazamKit.
    let outputFormat = AVAudioFormat(standardFormatWithSampleRate: 48000, channels: 1)
    
    // Create a mixer node to convert the input.
    audioEngine.attach(mixerNode)

    // Attach the mixer to the microphone input and the output of the audio engine.
    audioEngine.connect(audioEngine.inputNode, to: mixerNode, format: inputFormat)
    audioEngine.connect(mixerNode, to: audioEngine.outputNode, format: outputFormat)
        
    // Install a tap on the mixer node to capture the microphone audio.
    mixerNode.installTap(onBus: 0,
                         bufferSize: 8192,
                         format: outputFormat) { buffer, audioTime in
        // Add captured audio to the buffer used for making a match.
        self.addAudio(buffer: buffer, audioTime: audioTime)
    }
}
```

> **Note**:  The output from the built-in microphone on devices running iOS 14 and earlier is already in a format that’s compatible with ShazamKit. Other microphones or input sources may not be compatible.

##### Start and Stop the Audio Engine

Add a function to start listening to the microphone using the tap on the mixer node. You must request access to the microphone.

```swift
func startListening() throws {
    // Throw an error if the audio engine is already running.
    guard !audioEngine.isRunning else { return }
    let audioSession = AVAudioSession.sharedInstance()
    
    // Ask the user for permission to use the mic if required then start the engine.
    try audioSession.setCategory(.playAndRecord)
    audioSession.requestRecordPermission { [weak self] success in
        guard success, let self = self else { return }
        try? self.audioEngine.start()
    }
}
```

The category uses [`AVAudioRoutingArbiter.Category.playAndRecord`](https://developer.apple.com/documentation/AVFAudio/AVAudioRoutingArbiter/Category/playAndRecord) because the input of the mixer records the mic and the output plays the result. The tap captures the audio buffers from the output of the mixer.

Add another function to stop listening to the microphone. Call this function when you no longer need information about the matched item, such as the [`predictedCurrentMatchOffset`](shmatchedmediaitem/predictedcurrentmatchoffset.md). Also call this function when there’s a value for error in [`session(_:didNotFindMatchFor:error:)`](shsessiondelegate/session(_:didnotfindmatchfor:error:).md).

```swift
func stopListening() {
    // Check if the audio engine is already recording.
    if audioEngine.isRunning {
        audioEngine.stop()
    }
}

```

You can also [`pause()`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/pause()) the engine instead of stopping it.

##### Check for a Match in a Catalog

Check for a match by creating an [`SHSession`](shsession.md) object for a catalog and starting the audio engine. The following function demonstrates this:

```swift
func match(_ catalog: SHCustomCatalog) throws {
    // Create a session if one doesn't already exist.
    if (session == nil) {
        session = SHSession(catalog: catalog)
        session?.delegate = self
    }
    
    // Start listening to the audio to find a match.
    try startListening()
}
```

If your matcher uses multiple catalogs, you must create a new session when the catalog changes. The following function shows an example of this:

```swift
func match(_ catalog: SHCustomCatalog) throws {
    // Create a new session if there's an existing session with a different catalog.
    if session?.catalog != catalog {
        // Stop any active match request.
        stopListening()
        
        session = SHSession(catalog: catalog)
        session?.delegate = self
    }
    try startListening()
}
```

## See Also

- [func match(SHSignature)](shsession/match(_:).md)
  Searches for the query signature in the reference signatures that the session catalog contains.
- [func matchStreamingBuffer(AVAudioPCMBuffer, at: AVAudioTime?)](shsession/matchstreamingbuffer(_:at:).md)
  Converts the audio in the buffer to a signature, and searches the reference signatures in the session catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/matching-audio-using-the-built-in-microphone)*