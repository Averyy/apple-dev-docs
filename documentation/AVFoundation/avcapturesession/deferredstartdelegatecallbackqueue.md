# deferredStartDelegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which the session calls deferred start delegate methods.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var deferredStartDelegateCallbackQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t deferredStartDelegateCallbackQueue;
```

#### Discussion

Call the [`setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)`](./setdeferredstartdelegate%28_,deferredstartdelegatecallbackqueue%29.md) method to specify the dispatch queue on which to call the deferred start delegate methods.

## See Also

### Configuring deferred start
- [var isManualDeferredStartSupported: Bool](./ismanualdeferredstartsupported.md)
  A `BOOL` value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](./automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](./rundeferredstartwhenneeded%28%29.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](./deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](./setdeferredstartdelegate%28_,deferredstartdelegatecallbackqueue%29.md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/deferredstartdelegatecallbackqueue)*