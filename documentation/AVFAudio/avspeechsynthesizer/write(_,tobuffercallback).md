# write(_:toBufferCallback:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Generates speech for the utterance and invokes the callback with the audio buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func write(_ utterance: AVSpeechUtterance, toBufferCallback bufferCallback: @escaping AVSpeechSynthesizer.BufferCallback)
```

```objc
- (void) writeUtterance:(AVSpeechUtterance *) utterance toBufferCallback:(AVSpeechSynthesizerBufferCallback) bufferCallback;
```

## Discussion

Call this method to receive audio buffers to store or further process synthesized speech.

## Parameters

- `utterance`: The utterance for synthesizing speech.
- `bufferCallback`: The system calls this closure with the generated audio buffer.

## See Also

### Directing speech output
- [var usesApplicationAudioSession: Bool](./usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](./mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](./outputchannels.md)
  An array of audio session channels to route generated speech.
- [AVSpeechSynthesizer.BufferCallback](./buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](./write%28_,tobuffercallback,tomarkercallback%29.md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](./markercallback.md)
  A type that defines a callback that receives speech markers.
- [class AVSpeechSynthesisMarker](../avspeechsynthesismarker.md)
  An object that contains information about the synthesized audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/write(_:tobuffercallback:))*