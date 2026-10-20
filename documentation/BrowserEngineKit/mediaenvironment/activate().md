# activate()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Activates the media environment.

**Availability**:
- iOS 17.4+ - Deprecated in 27.0
- iPadOS 17.4+ - Deprecated in 27.0

> **Deprecated**: Use ProcessCapability.activate() instead

## Declaration

```swift
func activate() throws
```

## See Also

### Capturing media streams
- [func makeCaptureSession() throws -> AVCaptureSession](./makecapturesession%28%29.md)
  Creates a new capture session in this media environment  or throws an error if it can not be created.
- [func suspend() throws](./suspend%28%29.md)
  Suspends the media environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/mediaenvironment/activate())*