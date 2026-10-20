# AVCaptureOutput.DataDroppedReason

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureOutputDataDroppedReason : NSInteger;
```

## Topics

### Reasons
- [AVCaptureOutput.DataDroppedReason.none](./datadroppedreason/none.md)
  The system didn’t drop data.
- [AVCaptureOutput.DataDroppedReason.lateData](./datadroppedreason/latedata.md)
  The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutput.DataDroppedReason.outOfBuffers](./datadroppedreason/outofbuffers.md)
  The system dropped data because the capture output exhausted its internal pool of memory buffers.
- [AVCaptureOutput.DataDroppedReason.discontinuity](./datadroppedreason/discontinuity.md)
  The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.
### Initializers
- [init?(rawValue: Int)](./datadroppedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing connections
- [var connections: [AVCaptureConnection]](./connections.md)
  The capture output object’s connections.
- [func connection(with: AVMediaType) -> AVCaptureConnection?](./connection%28with%29.md)
  Returns the first connection with an input port of a specified media type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason)*