# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVCaptureDataOutputSynchronizerDelegate)?, queue delegateCallbackQueue: dispatch_queue_t?)
```

#### Discussion

The data output synchronizer gathers data from its data outputs, and when it determines that all data has been received for a given timestamp, it vends collections of synchronized data by calling delegate methods on the specified dispatch queue.

The [`AVCaptureDataOutputSynchronizer`](avcapturedataoutputsynchronizer.md) class overrides all the data outputs’ own delegates and callbacks. Data outputs under the control of a data output synchronizer do not fire delegate callbacks. Delegate callbacks are restored to individual data outputs only if you clear the synchronizer’s delegate and callback queue by calling this method and passing `nil` for both parameters.

## Parameters

- `delegate`: A delegate object to receive synchronized data.
- `delegateCallbackQueue`: The dispatch queue on which to call delegate methods. This parameter must be a serial dispatch queue to guarantee that captured data is delivered in order.

## See Also

- [var delegate: (any AVCaptureDataOutputSynchronizerDelegate)?](avcapturedataoutputsynchronizer/delegate.md)
  A delegate object that receives synchronized capture data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedataoutputsynchronizer/delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.
- [protocol AVCaptureDataOutputSynchronizerDelegate](avcapturedataoutputsynchronizerdelegate.md)
  Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/setdelegate(_:queue:))*