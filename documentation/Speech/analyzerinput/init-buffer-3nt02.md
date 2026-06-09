# init(buffer:)

**Framework**: Speech  
**Kind**: init

Creates an audio input object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(buffer: CMReadySampleBuffer<CMReadOnlyDataBlockBuffer>)
```

#### Discussion

The audio buffer must not overlap or precede other audio input, as determined by the buffer’s `presentationTimeStamp` value.

> 💡 **Tip**: To convert a `CMSampleBuffer` to a `CMReadySampleBuffer`, use `CMReadySampleBuffer(unsafeWithDataBuffer:)`. You should not alter the original `CMSampleBuffer` after passing it to that initializer.

## Parameters

- `buffer`: An audio buffer.

## See Also

- [init(buffer: AVAudioPCMBuffer)](analyzerinput/init(buffer:)-2ysg3.md)
  Creates an audio input object.
- [init(buffer: AVAudioPCMBuffer, bufferStartTime: CMTime?)](analyzerinput/init(buffer:bufferstarttime:).md)
  Creates an audio input object for audio that may be discontiguous with previous input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput/init(buffer:)-3nt02)*