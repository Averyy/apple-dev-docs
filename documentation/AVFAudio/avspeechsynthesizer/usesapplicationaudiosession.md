# usesApplicationAudioSession

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that specifies whether the app manages the audio session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var usesApplicationAudioSession: Bool { get set }
```

#### Discussion

If you set this value to [`false`](https://developer.apple.com/documentation/Swift/false), the system creates a separate audio session to automatically manage speech, interruptions, and mixing and ducking the speech with other audio sources.

## See Also

- [var mixToTelephonyUplink: Bool](avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](avspeechsynthesizer/outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](avspeechsynthesizer/write(_:tobuffercallback:).md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](avspeechsynthesizer/buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](avspeechsynthesizer/write(_:tobuffercallback:tomarkercallback:).md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/usesapplicationaudiosession)*