# append(_:)

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Appends audio in the PCM format to the end of the recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func append(_ audioPCMBuffer: AVAudioPCMBuffer)
```

```objc
- (void) appendAudioPCMBuffer:(AVAudioPCMBuffer *) audioPCMBuffer;
```

#### Discussion

The audio must be in a native format and uncompressed.

## Parameters

- `audioPCMBuffer`: An audio buffer that contains audio in the PCM format.

## See Also

### Appending Audio Buffers
- [func appendAudioSampleBuffer(CMSampleBuffer)](./appendaudiosamplebuffer%28_%29.md)
  Appends audio to the end of the recognition request.
- [func endAudio()](./endaudio%28%29.md)
  Marks the end of audio input for the recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest/append(_:))*