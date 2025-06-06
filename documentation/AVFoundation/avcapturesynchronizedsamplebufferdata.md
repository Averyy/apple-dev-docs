# AVCaptureSynchronizedSampleBufferData

**Framework**: AVFoundation  
**Kind**: class

A container for video or audio samples collected using synchronized capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureSynchronizedSampleBufferData
```

## Topics

### Accessing Synchronized Data
- [var sampleBuffer: CMSampleBuffer](avcapturesynchronizedsamplebufferdata/samplebuffer.md)
  The depth data captured at this synchronization point.
### Handling Dropped Data
- [var sampleBufferWasDropped: Bool](avcapturesynchronizedsamplebufferdata/samplebufferwasdropped.md)
  A Boolean value indicating whether sample buffers were discarded between capture and processing.
- [var droppedReason: AVCaptureOutput.DataDroppedReason](avcapturesynchronizedsamplebufferdata/droppedreason.md)
  A value indicating why the capture output failed to deliver sample buffers, if applicable.

## Relationships

### Inherits From
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md)
  An object that coordinates time-matched delivery of data from multiple capture outputs.
- [class AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md)
  A set of data samples collected simultaneously from multiple capture outputs.
- [class AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.
- [class AVCaptureSynchronizedData](avcapturesynchronizeddata.md)
  The abstract superclass for media samples collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata)*