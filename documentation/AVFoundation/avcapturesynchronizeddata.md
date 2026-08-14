# AVCaptureSynchronizedData

**Framework**: AVFoundation  
**Kind**: class

The abstract superclass for media samples collected using synchronized capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureSynchronizedData
```

## Topics

### Correlating synchronized data
- [var timestamp: CMTime](avcapturesynchronizeddata/timestamp.md)
  The time at which this synchronized data was captured.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md)
  An object that coordinates time-matched delivery of data from multiple capture outputs.
- [class AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md)
  A set of data samples collected simultaneously from multiple capture outputs.
- [class AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)
  A container for video or audio samples collected using synchronized capture.
- [class AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddata)*