# AVCaptureDataOutputSynchronizer

**Framework**: AVFoundation  
**Kind**: class

An object that coordinates time-matched delivery of data from multiple capture outputs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureDataOutputSynchronizer
```

#### Overview

Use this class when you need to capture media from multiple capture outputs and want to receive all data samples from the same timestamp in a single delegate callback.

For example, when you use an [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) object to coordinate the output of [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) and [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) objects, you can easily match each captured video frame to depth information captured at the same moment.

## Topics

### Configuring synchronized capture
- [init(dataOutputs: [AVCaptureOutput])](avcapturedataoutputsynchronizer/init(dataoutputs:).md)
  Creates a capture output synchronizer for the specified capture outputs.
- [var dataOutputs: [AVCaptureOutput]](avcapturedataoutputsynchronizer/dataoutputs.md)
  The list of data outputs governed by this data output synchronizer.
### Receiving synchronized capture data
- [func setDelegate((any AVCaptureDataOutputSynchronizerDelegate)?, queue: dispatch_queue_t?)](avcapturedataoutputsynchronizer/setdelegate(_:queue:).md)
  Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [var delegate: (any AVCaptureDataOutputSynchronizerDelegate)?](avcapturedataoutputsynchronizer/delegate.md)
  A delegate object that receives synchronized capture data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedataoutputsynchronizer/delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.
- [protocol AVCaptureDataOutputSynchronizerDelegate](avcapturedataoutputsynchronizerdelegate.md)
  Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md)
  A set of data samples collected simultaneously from multiple capture outputs.
- [class AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md)
  A container for video or audio samples collected using synchronized capture.
- [class AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md)
  A container for metadata objects collected using synchronized capture.
- [class AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md)
  A container for scene depth information collected using synchronized capture.
- [class AVCaptureSynchronizedData](avcapturesynchronizeddata.md)
  The abstract superclass for media samples collected using synchronized capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer)*