# AVCaptureDataOutputSynchronizerDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol AVCaptureDataOutputSynchronizerDelegate <NSObject>
```

## Topics

### Receiving synchronized capture data
- [func dataOutputSynchronizer(AVCaptureDataOutputSynchronizer, didOutput: AVCaptureSynchronizedDataCollection)](./avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer%28_,didoutput%29.md)
  Provides a collection of synchronized capture data to the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Receiving synchronized capture data
- [func setDelegate((any AVCaptureDataOutputSynchronizerDelegate)?, queue: dispatch_queue_t?)](./avcapturedataoutputsynchronizer/setdelegate%28_,queue%29.md)
  Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [var delegate: (any AVCaptureDataOutputSynchronizerDelegate)?](./avcapturedataoutputsynchronizer/delegate.md)
  A delegate object that receives synchronized capture data.
- [var delegateCallbackQueue: dispatch_queue_t?](./avcapturedataoutputsynchronizer/delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate)*