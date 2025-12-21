# isManualDeferredStartSupported

**Framework**: AVFoundation  
**Kind**: property

A `BOOL` value that indicates whether the session supports manually running deferred start.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isManualDeferredStartSupported: Bool { get }
```

#### Discussion

Deferred Start is a feature that allows you to control, on a per-output basis, whether output objects start when or after the session is started. The session defers starting an output when its `deferredStartEnabled` property is set to `true`, and starts it after the session is started.

You can only set the [`automaticallyRunsDeferredStart`](avcapturesession/automaticallyrunsdeferredstart.md) property value to `false` if the session supports manual deferred start.

## See Also

- [var automaticallyRunsDeferredStart: Bool](avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](avcapturesession/rundeferredstartwhenneeded.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](avcapturesession/deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [var deferredStartDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/deferredstartdelegatecallbackqueue.md)
  The dispatch queue on which the session calls deferred start delegate methods.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/ismanualdeferredstartsupported)*