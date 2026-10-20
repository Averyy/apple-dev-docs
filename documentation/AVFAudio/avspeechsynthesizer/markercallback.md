# AVSpeechSynthesizer.MarkerCallback

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A type that defines a callback that receives speech markers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
typealias MarkerCallback = ([AVSpeechSynthesisMarker]) -> Void
```

```c
typedef void (^)(NSArray<AVSpeechSynthesisMarker *> *) AVSpeechSynthesizerMarkerCallback;
```

## Parameters

- `markers`: An array of speech synthesis markers.

## See Also

### Directing speech output
- [var usesApplicationAudioSession: Bool](./usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](./mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](./outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](./write%28_,tobuffercallback%29.md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](./buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](./write%28_,tobuffercallback,tomarkercallback%29.md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [class AVSpeechSynthesisMarker](../avspeechsynthesismarker.md)
  An object that contains information about the synthesized audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/markercallback)*