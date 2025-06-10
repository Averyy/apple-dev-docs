# setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)

**Framework**: AVFoundation  
**Kind**: method

Sets a delegate object for the session to call when performing deferred start.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func setDeferredStartDelegate(_ deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)
```

#### Discussion

This delegate receives a call to the `sessionWillRunDeferredStart` method when deferred start is about to run. It is non-blocking, so it’s also possible that by the time this method is called, the deferred start is already underway. If you want your app to perform initialization (potentially) concurrently with deferred start (e.g. user-facing camera features that are not needed to display the first preview frame, but are available to the user as soon as possible) it may be done in the delegate’s `sessionWillRunDeferredStart` method. To wait until deferred start is finished to perform some remaining initialization work, use the `sessionDidRunDeferredStart` method instead.

The delegate receives a call to the `sessionDidRunDeferredStart` method when the deferred start finishes running. This allows you to run less-critical application initialization code. For example, if you’ve deferred an [`AVCapturePhotoOutput`](avcapturephotooutput.md) by setting its `deferredStartEnabled` property to `true`, and you’d like to do some app-specific initialization related to still capture, here might be a good place to put it.

If the delegate is non-nil, the session still calls the `sessionWillRunDeferredStart` and `sessionDidRunDeferredStart` methods regardless of the value of the session’s [`automaticallyRunsDeferredStart`](avcapturesession/automaticallyrunsdeferredstart.md) property.

To minimize the capture session’s startup latency, defer all unnecessary work until after the session starts. This delegate provides callbacks for you to schedule deferred work without impacting session startup performance.

To perform initialization prior to deferred start but after the user interface displays, set [`automaticallyRunsDeferredStart`](avcapturesession/automaticallyrunsdeferredstart.md) to `false`, and then run the custom initialization prior to calling [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md).

If [`deferredStartDelegate`](avcapturesession/deferredstartdelegate.md) is not `NULL`, the session throws an exception if [`deferredStartDelegateCallbackQueue`](avcapturesession/deferredstartdelegatecallbackqueue.md) is `nil`.

## Parameters

- `deferredStartDelegate`: An object conforming to the ‘AVCaptureSessionDeferredStartDelegate’ protocol that receives events about deferred start.
- `deferredStartDelegateCallbackQueue`: A dispatch queue on which deferredStart delegate methods are called.

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
- [protocol AVCaptureSessionDeferredStartDelegate](avcapturesessiondeferredstartdelegate.md)
  A protocol that defines the interface to respond to events about a capture session’s deferred start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:))*