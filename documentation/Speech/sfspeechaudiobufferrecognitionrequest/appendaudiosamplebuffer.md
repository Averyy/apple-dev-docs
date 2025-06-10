# appendAudioSampleBuffer(_:)

**Framework**: Speech  
**Kind**: method

Appends audio to the end of the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func appendAudioSampleBuffer(_ sampleBuffer: CMSampleBuffer)
```

#### Discussion

The audio must be in a native format.

## Parameters

- `sampleBuffer`: A buffer of audio.

## See Also

- [func append(AVAudioPCMBuffer)](sfspeechaudiobufferrecognitionrequest/append(_:).md)
  Appends audio in the PCM format to the end of the recognition request.
- [func endAudio()](sfspeechaudiobufferrecognitionrequest/endaudio.md)
  Marks the end of audio input for the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/appendaudiosamplebuffer(_:))*