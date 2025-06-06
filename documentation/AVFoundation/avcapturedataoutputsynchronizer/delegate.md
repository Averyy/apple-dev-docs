# delegate

**Framework**: AVFoundation  
**Kind**: property

A delegate object that receives synchronized capture data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var delegate: (any AVCaptureDataOutputSynchronizerDelegate)? { get }
```

#### Discussion

This property is read-only. You set the delegate object and the dispatch queue for delegate methods together using the [`setDelegate(_:queue:)`](avcapturedataoutputsynchronizer/setdelegate(_:queue:).md) method.

## See Also

- [func setDelegate((any AVCaptureDataOutputSynchronizerDelegate)?, queue: dispatch_queue_t?)](avcapturedataoutputsynchronizer/setdelegate(_:queue:).md)
  Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedataoutputsynchronizer/delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.
- [protocol AVCaptureDataOutputSynchronizerDelegate](avcapturedataoutputsynchronizerdelegate.md)
  Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/delegate)*