# AVCaptureSessionDeferredStartDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the interface to respond to events about a capture session’s deferred start.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
protocol AVCaptureSessionDeferredStartDelegate : NSObjectProtocol
```

```objc
@protocol AVCaptureSessionDeferredStartDelegate <NSObject>
```

## Topics

### Responding to deferred start events
- [func sessionDidRunDeferredStart(AVCaptureSession)](./avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart%28_%29.md)
  This method gets called by the session when deferred start has finished running.
- [func sessionWillRunDeferredStart(AVCaptureSession)](./avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart%28_%29.md)
  This method gets called by the session when deferred start is about to run.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring deferred start
- [var isManualDeferredStartSupported: Bool](./avcapturesession/ismanualdeferredstartsupported.md)
  A `BOOL` value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](./avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](./avcapturesession/rundeferredstartwhenneeded%28%29.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](./avcapturesession/deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [var deferredStartDelegateCallbackQueue: dispatch_queue_t?](./avcapturesession/deferredstartdelegatecallbackqueue.md)
  The dispatch queue on which the session calls deferred start delegate methods.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](./avcapturesession/setdeferredstartdelegate%28_,deferredstartdelegatecallbackqueue%29.md)
  Sets a delegate object for the session to call when performing deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate)*