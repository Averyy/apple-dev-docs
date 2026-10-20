# mixToTelephonyUplink

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to send synthesized speech to an active call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mixToTelephonyUplink: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL mixToTelephonyUplink;
```

#### Discussion

This property has no effect when there isn’t an active call.

## See Also

### Directing speech output
- [var usesApplicationAudioSession: Bool](./usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var outputChannels: [AVAudioSessionChannelDescription]?](./outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](./write%28_,tobuffercallback%29.md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](./buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](./write%28_,tobuffercallback,tomarkercallback%29.md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](./markercallback.md)
  A type that defines a callback that receives speech markers.
- [class AVSpeechSynthesisMarker](../avspeechsynthesismarker.md)
  An object that contains information about the synthesized audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/mixtotelephonyuplink)*