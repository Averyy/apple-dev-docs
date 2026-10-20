# AVCaptureSynchronizedMetadataObjectData

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A container for metadata objects collected using synchronized capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureSynchronizedMetadataObjectData
```

```objc
@interface AVCaptureSynchronizedMetadataObjectData : AVCaptureSynchronizedData
```

## Topics

### Accessing synchronized data
- [var metadataObjects: [AVMetadataObject]](./avcapturesynchronizedmetadataobjectdata/metadataobjects.md)
  The list of metadata objects captured at this synchronization timestamp.

## Relationships

### Inherits From
- [AVCaptureSynchronizedData](./avcapturesynchronizeddata.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Synchronized capture
- [class AVCaptureDataOutputSynchronizer](./avcapturedataoutputsynchronizer.md)
  An object that coordinates time-matched delivery of data from multiple capture outputs.
- [class AVCaptureSynchronizedDataCollection](./avcapturesynchronizeddatacollection.md)
  A set of data samples collected simultaneously from multiple capture outputs.
- [class AVCaptureSynchronizedSampleBufferData](./avcapturesynchronizedsamplebufferdata.md)
  A container for video or audio samples collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](./avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.
- [class AVCaptureSynchronizedData](./avcapturesynchronizeddata.md)
  The abstract superclass for media samples collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedmetadataobjectdata)*