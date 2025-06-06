# endAudio()

**Framework**: Speech  
**Kind**: method

Marks the end of audio input for the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func endAudio()
```

#### Discussion

Call this method explicitly to let the speech recognizer know that no more audio input is coming.

## See Also

- [func append(AVAudioPCMBuffer)](sfspeechaudiobufferrecognitionrequest/append(_:).md)
  Appends audio in the PCM format to the end of the recognition request.
- [func appendAudioSampleBuffer(CMSampleBuffer)](sfspeechaudiobufferrecognitionrequest/appendaudiosamplebuffer(_:).md)
  Appends audio to the end of the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/endaudio())*