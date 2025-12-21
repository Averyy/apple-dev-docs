# deferredStartDelegate

**Framework**: AVFoundation  
**Kind**: property

A delegate object that observes events about deferred start.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)? { get }
```

#### Discussion

Call the [`setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)`](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md) method to set the deferred start delegate for a session.

## See Also

- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A `BOOL` value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](avcapturesession/rundeferredstartwhenneeded.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/deferredstartdelegatecallbackqueue.md)
  The dispatch queue on which the session calls deferred start delegate methods.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/deferredstartdelegate)*