# AVSpeechSynthesizer.BufferCallback

**Framework**: AVFAudio  
**Kind**: typealias

A type that defines a callback that receives a buffer of generated speech.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias BufferCallback = (AVAudioBuffer) -> Void
```

## See Also

- [var usesApplicationAudioSession: Bool](avspeechsynthesizer/usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](avspeechsynthesizer/outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](avspeechsynthesizer/write(_:tobuffercallback:).md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](avspeechsynthesizer/write(_:tobuffercallback:tomarkercallback:).md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/buffercallback)*