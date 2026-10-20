# sessionDidRunDeferredStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This method gets called by the session when deferred start has finished running.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func sessionDidRunDeferredStart(_ session: AVCaptureSession)
```

```objc
- (void) sessionDidRunDeferredStart:(AVCaptureSession *) session;
```

## Parameters

- `session`: The [`AVCaptureSession`](../avcapturesession.md) instance that runs the deferred start.

## See Also

### Responding to deferred start events
- [func sessionWillRunDeferredStart(AVCaptureSession)](./sessionwillrundeferredstart%28_%29.md)
  This method gets called by the session when deferred start is about to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:))*