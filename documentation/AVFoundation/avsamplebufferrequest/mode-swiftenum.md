# AVSampleBufferRequest.Mode

**Framework**: AVFoundation  
**Kind**: enum

The modes in which a sample buffer generator processes a request.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Mode
```

## Topics

### Mode Scheduling
- [AVSampleBufferRequest.Mode.immediate](avsamplebufferrequest/mode-swift.enum/immediate.md)
  A mode that indicates that sample buffer creation requests load data as soon as possible.
- [AVSampleBufferRequest.Mode.scheduled](avsamplebufferrequest/mode-swift.enum/scheduled.md)
  A mode that indicates that sample buffer creation requests load data according to a scheduled deadline.
- [AVSampleBufferRequest.Mode.opportunistic](avsamplebufferrequest/mode-swift.enum/opportunistic.md)
  A mode that indicates that opportunistic sample buffer creation requests load data as soon as possible.
### Initializers
- [init?(rawValue: Int)](avsamplebufferrequest/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var direction: AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.property.md)
  The buffer sample direction.
- [AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.enum.md)
  The modes that describe the buffer request direction.
- [var limitCursor: AVSampleCursor?](avsamplebufferrequest/limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](avsamplebufferrequest/maxsamplecount.md)
  The maximum number of samples to load.
- [var mode: AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.property.md)
  The sample buffer request mode.
- [var overrideTime: CMTime](avsamplebufferrequest/overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](avsamplebufferrequest/preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](avsamplebufferrequest/startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum)*