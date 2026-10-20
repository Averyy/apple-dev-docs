# AVCaptureSynchronizedData

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptureSynchronizedData : NSObject
```

## Topics

### Correlating synchronized data
- [var timestamp: CMTime](./avcapturesynchronizeddata/timestamp.md)
  The time at which this synchronized data was captured.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVCaptureSynchronizedDepthData](./avcapturesynchronizeddepthdata.md)
- [AVCaptureSynchronizedMetadataObjectData](./avcapturesynchronizedmetadataobjectdata.md)
- [AVCaptureSynchronizedSampleBufferData](./avcapturesynchronizedsamplebufferdata.md)
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
- [class AVCaptureSynchronizedMetadataObjectData](./avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](./avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddata)*