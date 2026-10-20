# makeCaptureSession()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a new capture session in this media environment  or throws an error if it can not be created.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func makeCaptureSession() throws -> AVCaptureSession
```

#### Discussion

The media environment must be activated before the capture session can be started.

## See Also

### Capturing media streams
- [func activate() throws](./activate%28%29.md)
  Activates the media environment.
- [func suspend() throws](./suspend%28%29.md)
  Suspends the media environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/mediaenvironment/makecapturesession())*