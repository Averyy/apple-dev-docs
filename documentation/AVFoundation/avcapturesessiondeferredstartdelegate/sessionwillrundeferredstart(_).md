# sessionWillRunDeferredStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This method gets called by the session when deferred start is about to run.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func sessionWillRunDeferredStart(_ session: AVCaptureSession)
```

```objc
- (void) sessionWillRunDeferredStart:(AVCaptureSession *) session;
```

## Discussion

Delegates receive this message when the session has finished the deferred start. This message will be sent regardless of whether the session’s [`automaticallyRunsDeferredStart`](../avcapturesession/automaticallyrunsdeferredstart.md) property is set. See [`setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)`](../avcapturesession/setdeferredstartdelegate%28_,deferredstartdelegatecallbackqueue%29.md) documentation for more information.

## Parameters

- `session`: The [`AVCaptureSession`](../avcapturesession.md) instance that runs the deferred start.

## See Also

### Responding to deferred start events
- [func sessionDidRunDeferredStart(AVCaptureSession)](./sessiondidrundeferredstart%28_%29.md)
  This method gets called by the session when deferred start has finished running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:))*