# endAudio()

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Marks the end of audio input for the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func endAudio()
```

```objc
- (void) endAudio;
```

#### Discussion

Call this method explicitly to let the speech recognizer know that no more audio input is coming.

## See Also

### Appending Audio Buffers
- [func append(AVAudioPCMBuffer)](./append%28_%29.md)
  Appends audio in the PCM format to the end of the recognition request.
- [func appendAudioSampleBuffer(CMSampleBuffer)](./appendaudiosamplebuffer%28_%29.md)
  Appends audio to the end of the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/endaudio())*