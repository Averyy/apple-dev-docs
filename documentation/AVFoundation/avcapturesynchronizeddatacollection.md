# AVCaptureSynchronizedDataCollection

**Framework**: AVFoundation  
**Kind**: class

A set of data samples collected simultaneously from multiple capture outputs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureSynchronizedDataCollection
```

## Topics

### Accessing Synchronized Data
- [var count: Int](avcapturesynchronizeddatacollection/count.md)
  The number of synchronized data objects in the collection.
- [func synchronizedData(for: AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/synchronizeddata(for:).md)
  Returns synchronized data captured by the specified capture output.
- [subscript(AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/subscript(_:).md)
  Returns data captured by the specified capture output, using subscript syntax.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md)
  An object that coordinates time-matched delivery of data from multiple capture outputs.
- [class AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)
  A container for video or audio samples collected using synchronized capture.
- [class AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.
- [class AVCaptureSynchronizedData](avcapturesynchronizeddata.md)
  The abstract superclass for media samples collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection)*