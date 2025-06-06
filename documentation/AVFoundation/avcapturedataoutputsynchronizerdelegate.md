# AVCaptureDataOutputSynchronizerDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
protocol AVCaptureDataOutputSynchronizerDelegate : NSObjectProtocol
```

## Topics

### Receiving Synchronized Capture Data
- [func dataOutputSynchronizer(AVCaptureDataOutputSynchronizer, didOutput: AVCaptureSynchronizedDataCollection)](avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(_:didoutput:).md)
  Provides a collection of synchronized capture data to the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setDelegate((any AVCaptureDataOutputSynchronizerDelegate)?, queue: dispatch_queue_t?)](avcapturedataoutputsynchronizer/setdelegate(_:queue:).md)
  Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [var delegate: (any AVCaptureDataOutputSynchronizerDelegate)?](avcapturedataoutputsynchronizer/delegate.md)
  A delegate object that receives synchronized capture data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedataoutputsynchronizer/delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate)*