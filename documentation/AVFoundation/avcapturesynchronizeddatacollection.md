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

### Accessing synchronized data
- [var count: Int](avcapturesynchronizeddatacollection/count.md)
  The number of synchronized data objects in the collection.
- [func synchronizedData(for: AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/synchronizeddata(for:).md)
  Returns synchronized data captured by the specified capture output.
- [subscript(AVCaptureOutput) -> AVCaptureSynchronizedData?](avcapturesynchronizeddatacollection/subscript(_:).md)
  Returns data captured by the specified capture output, using subscript syntax.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSFastEnumeration](../foundation/nsfastenumeration.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sequence](../swift/sequence.md)

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