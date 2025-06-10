# AVSampleBufferRequest.Direction

**Framework**: AVFoundation  
**Kind**: enum

The modes that describe the buffer request direction.

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
enum Direction
```

## Topics

### Buffer Direction
- [AVSampleBufferRequest.Direction.forward](avsamplebufferrequest/direction-swift.enum/forward.md)
  The number of following samples may be zero or greater.
- [AVSampleBufferRequest.Direction.none](avsamplebufferrequest/direction-swift.enum/none.md)
  A single sample will be loaded.
- [AVSampleBufferRequest.Direction.reverse](avsamplebufferrequest/direction-swift.enum/reverse.md)
  The number of previous samples may be zero or greater.
### Initializers
- [init?(rawValue: Int)](avsamplebufferrequest/direction-swift.enum/init(rawvalue:).md)

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
- [var limitCursor: AVSampleCursor?](avsamplebufferrequest/limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](avsamplebufferrequest/maxsamplecount.md)
  The maximum number of samples to load.
- [var mode: AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.property.md)
  The sample buffer request mode.
- [AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.enum.md)
  The modes in which a sample buffer generator processes a request.
- [var overrideTime: CMTime](avsamplebufferrequest/overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](avsamplebufferrequest/preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](avsamplebufferrequest/startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum)*