# sessionWillRunDeferredStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

This method gets called by the session when deferred start is about to run.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func sessionWillRunDeferredStart(_ session: AVCaptureSession)
```

#### Discussion

Delegates receive this message when the session has finished the deferred start. This message will be sent regardless of whether the session’s automaticallyRunsDeferredStart property is set. See `setDeferredStartDelegate:queue:` documentation for more information.

## Parameters

- `session`: The   instance that runs the deferred start.

## See Also

- [func sessionDidRunDeferredStart(AVCaptureSession)](avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:).md)
  This method gets called by the session when deferred start has finished running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:))*