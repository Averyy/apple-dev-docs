# AVSampleBufferRequest.Mode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

The modes in which a sample buffer generator processes a request.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum Mode
```

```c
enum AVSampleBufferRequestMode : NSInteger;
```

## Topics

### Mode scheduling
- [AVSampleBufferRequest.Mode.immediate](./mode-swift.enum/immediate.md)
  A mode that indicates that sample buffer creation requests load data as soon as possible.
- [AVSampleBufferRequest.Mode.scheduled](./mode-swift.enum/scheduled.md)
  A mode that indicates that sample buffer creation requests load data according to a scheduled deadline.
- [AVSampleBufferRequest.Mode.opportunistic](./mode-swift.enum/opportunistic.md)
  A mode that indicates that opportunistic sample buffer creation requests load data as soon as possible.
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring sample buffer request parameters
- [var direction: AVSampleBufferRequest.Direction](./direction-swift.property.md)
  The buffer sample direction.
- [AVSampleBufferRequest.Direction](./direction-swift.enum.md)
  The modes that describe the buffer request direction.
- [var limitCursor: AVSampleCursor?](./limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](./maxsamplecount.md)
  The maximum number of samples to load.
- [var mode: AVSampleBufferRequest.Mode](./mode-swift.property.md)
  The sample buffer request mode.
- [var overrideTime: CMTime](./overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](./preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](./startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum)*