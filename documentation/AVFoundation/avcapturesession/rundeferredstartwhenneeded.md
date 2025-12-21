# runDeferredStartWhenNeeded()

**Framework**: AVFoundation  
**Kind**: method

Tells the session to run deferred start when appropriate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func runDeferredStartWhenNeeded()
```

#### Discussion

For best perceived startup performance, call this after displaying the first frame, so that deferred start processing doesn’t interfere with other initialization operations. For example, if using a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) to draw camera frames, add a `presentHandler` (using doc://com.apple.documentation/metal/mtldrawable/addpresentedhandler) to the first drawable and call [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md) from there.

If one or more outputs need to start to perform a capture operation, and [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md) has not run yet, the session runs the deferred start on your app’s behalf. Only call this method once for each configuration commit - after the first call, subsequent calls to [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md) have no effect. The deferred start runs asynchronously, so this method returns immediately.

> **Note**: You can only call this when [`automaticallyRunsDeferredStart`](avcapturesession/automaticallyrunsdeferredstart.md) is `false`. Otherwise, the session throws an `NSInvalidArgumentException`.

> ❗ **Important**: To avoid blocking your app’s UI, don’t call this method from the application’s main actor or queue.

## See Also

- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A `BOOL` value that indicates whether the session supports manually running deferred start.
- [var automaticallyRunsDeferredStart: Bool](avcapturesession/automaticallyrunsdeferredstart.md)
  A Boolean value that indicates whether deferred start runs automatically.
- [var deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?](avcapturesession/deferredstartdelegate.md)
  A delegate object that observes events about deferred start.
- [var deferredStartDelegateCallbackQueue: dispatch_queue_t?](avcapturesession/deferredstartdelegatecallbackqueue.md)
  The dispatch queue on which the session calls deferred start delegate methods.
- [func setDeferredStartDelegate((any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)](avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:).md)
  Sets a delegate object for the session to call when performing deferred start.
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/rundeferredstartwhenneeded())*