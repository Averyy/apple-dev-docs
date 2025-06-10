# AVCaptureOutput.DataDroppedReason

**Framework**: AVFoundation  
**Kind**: enum

Constants that define reasons for why the system dropped a frame.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum DataDroppedReason
```

## Topics

### Reasons
- [AVCaptureOutput.DataDroppedReason.none](avcaptureoutput/datadroppedreason/none.md)
  The system didn’t drop data.
- [AVCaptureOutput.DataDroppedReason.lateData](avcaptureoutput/datadroppedreason/latedata.md)
  The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutput.DataDroppedReason.outOfBuffers](avcaptureoutput/datadroppedreason/outofbuffers.md)
  The system dropped data because the capture output exhausted its internal pool of memory buffers.
- [AVCaptureOutput.DataDroppedReason.discontinuity](avcaptureoutput/datadroppedreason/discontinuity.md)
  The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.
### Initializers
- [init?(rawValue: Int)](avcaptureoutput/datadroppedreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var connections: [AVCaptureConnection]](avcaptureoutput/connections.md)
  The capture output object’s connections.
- [func connection(with: AVMediaType) -> AVCaptureConnection?](avcaptureoutput/connection(with:).md)
  Returns the first connection with an input port of a specified media type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason)*