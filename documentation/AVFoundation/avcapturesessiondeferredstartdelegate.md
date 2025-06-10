# AVCaptureSessionDeferredStartDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the interface to respond to events about a capture session’s deferred start.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
protocol AVCaptureSessionDeferredStartDelegate : NSObjectProtocol
```

## Topics

### Responding to deferred start events
- [func sessionDidRunDeferredStart(AVCaptureSession)](avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:).md)
  This method gets called by the session when deferred start has finished running.
- [func sessionWillRunDeferredStart(AVCaptureSession)](avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:).md)
  This method gets called by the session when deferred start is about to run.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A Boolean value that indicates whether the session supports manually running deferred start.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate)*