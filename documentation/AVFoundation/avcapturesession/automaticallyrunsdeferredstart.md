# automaticallyRunsDeferredStart

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether deferred start runs automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var automaticallyRunsDeferredStart: Bool { get set }
```

#### Discussion

Deferred Start is a feature that allows you to control, on a per-output basis, whether output objects start when or after the session is started. The session defers starting an output when its [`isDeferredStartEnabled`](avcaptureoutput/isdeferredstartenabled.md) property is set to `true`, and starts it after the session is started.

When this value is `true`, [`AVCaptureSession`](avcapturesession.md) automatically runs deferred start. If only [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) objects have [`isDeferredStartEnabled`](avcapturevideopreviewlayer/isdeferredstartenabled.md) set to `false`, the session runs deferred start a short time after displaying the first frame. If there are [`AVCaptureOutput`](avcaptureoutput.md) objects that have [`isDeferredStartEnabled`](avcaptureoutput/isdeferredstartenabled.md) set to `false`, then the session waits until each output that provides streaming data to your app sends its first frame.

If you set this value to `false`, call [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md) to indicate when to run deferred start.

By default, for apps that are linked on or after iOS 26, this value is `true`.

If [`isManualDeferredStartSupported`](avcapturesession/ismanualdeferredstartsupported.md) is `false`, setting this property value to false results in the session throwing an invalid argument exception.

## See Also

- [var isManualDeferredStartSupported: Bool](avcapturesession/ismanualdeferredstartsupported.md)
  A `BOOL` value that indicates whether the session supports manually running deferred start.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyrunsdeferredstart)*