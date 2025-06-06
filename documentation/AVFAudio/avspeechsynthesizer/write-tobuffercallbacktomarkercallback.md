# write(_:toBufferCallback:toMarkerCallback:)

**Framework**: AVFAudio  
**Kind**: method

Generates audio buffers and associated metadata for storage or further speech synthesis processing.

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
func write(_ utterance: AVSpeechUtterance, toBufferCallback bufferCallback: @escaping AVSpeechSynthesizer.BufferCallback, toMarkerCallback markerCallback: @escaping AVSpeechSynthesizer.MarkerCallback)
```

## Parameters

- `utterance`: A utterance for a synthesizer to speak.
- `bufferCallback`: A callback that the system invokes with the synthesized audio data.
- `markerCallback`: A callback that the system invokes with marker information.

## See Also

- [var usesApplicationAudioSession: Bool](avspeechsynthesizer/usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](avspeechsynthesizer/outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](avspeechsynthesizer/write(_:tobuffercallback:).md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](avspeechsynthesizer/buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [AVSpeechSynthesizer.MarkerCallback](avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/write(_:tobuffercallback:tomarkercallback:))*