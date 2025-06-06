# outputChannels

**Framework**: AVFAudio  
**Kind**: property

An array of audio session channels to route generated speech.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var outputChannels: [AVAudioSessionChannelDescription]? { get set }
```

#### Discussion

The system replicates speech audio to each audio session channel.

## See Also

- [var usesApplicationAudioSession: Bool](avspeechsynthesizer/usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](avspeechsynthesizer/write(_:tobuffercallback:).md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](avspeechsynthesizer/buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](avspeechsynthesizer/write(_:tobuffercallback:tomarkercallback:).md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/outputchannels)*