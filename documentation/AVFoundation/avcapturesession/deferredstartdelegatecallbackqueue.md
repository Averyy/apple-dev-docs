# deferredStartDelegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which the session calls deferred start delegate methods.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var deferredStartDelegateCallbackQueue: dispatch_queue_t? { get }
```

#### Discussion

Call the `setDeferredStartDelegate:queue:` method to specify the dispatch queue on which to call the deferred start delegate methods.

## See Also

- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A Boolean value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [func runDeferredStartWhenNeeded()](avcapturesession/rundeferredstartwhenneeded.md)
  Tells the session to run deferred start when appropriate.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](avcapturesession/deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/deferredstartdelegatecallbackqueue)*