# sessionDidRunDeferredStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
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

## Parameters

- `session`: The   instance that runs the deferred start.

## See Also

- [func sessionWillRunDeferredStart(AVCaptureSession)](avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:).md)
  This method gets called by the session when deferred start is about to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:))*