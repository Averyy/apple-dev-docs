# AVFAudio

**Framework**: AVFAudio  
**Kind**: module

Play, record, and process audio; configure your app’s system audio behavior.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Topics

### Essentials
- [AVFAudio updates](../Updates/AVFAudio.md)
  Learn about important changes to AVFAudio.
### System audio
- [Handling audio interruptions](handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Routing audio to specific devices in multidevice sessions](routing-audio-to-specific-devices-in-multidevice-sessions.md)
  Map audio channels to specific devices in multiroute sessions for recording and playback.
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
### Basic playback and recording
- [class AVAudioPlayer](avaudioplayer.md)
  An object that plays audio data from a file or buffer.
- [class AVAudioRecorder](avaudiorecorder.md)
  An object that records audio data to a file.
- [class AVMIDIPlayer](avmidiplayer.md)
  An object that plays MIDI data through a system sound module.
### Advanced audio processing
- [Audio Engine](audio-engine.md)
  Perform advanced real-time and offline audio processing, implement 3D spatialization, and work with MIDI and samplers.
### Speech synthesis
- [Speech synthesis](speech-synthesis.md)
  Configure voices to speak strings of text.
### Macros
- [Macros](macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFAudio)*