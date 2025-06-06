# delegate

**Framework**: AVFoundation  
**Kind**: property

A delegate object that receives depth data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var delegate: (any AVCaptureDepthDataOutputDelegate)? { get }
```

#### Discussion

This property is read-only. You set the delegate object and the dispatch queue for calling delegate methods together using the [`setDelegate(_:callbackQueue:)`](avcapturedepthdataoutput/setdelegate(_:callbackqueue:).md) method.

## See Also

- [func setDelegate((any AVCaptureDepthDataOutputDelegate)?, callbackQueue: dispatch_queue_t?)](avcapturedepthdataoutput/setdelegate(_:callbackqueue:).md)
  Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedepthdataoutput/delegatecallbackqueue.md)
  A dispatch queue for delivering depth data.
- [protocol AVCaptureDepthDataOutputDelegate](avcapturedepthdataoutputdelegate.md)
  Methods for receiving depth data produced by a depth capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/delegate)*