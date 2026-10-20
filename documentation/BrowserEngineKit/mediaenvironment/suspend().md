# suspend()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Suspends the media environment.

**Availability**:
- iOS 17.4+ - Deprecated in 27.0
- iPadOS 17.4+ - Deprecated in 27.0

> **Deprecated**: Use ProcessCapability.suspend() instead

## Declaration

```swift
func suspend() throws
```

## See Also

### Capturing media streams
- [func activate() throws](./activate%28%29.md)
  Activates the media environment.
- [func makeCaptureSession() throws -> AVCaptureSession](./makecapturesession%28%29.md)
  Creates a new capture session in this media environment  or throws an error if it can not be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/mediaenvironment/suspend())*