# finish()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Requests that the capture session be stopped and all data saved.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func finish()
```

#### Discussion

Call this method when the user has completed the scan successfully.  The session switches to state `.finishing` while it saves all data and ultimately switches the state to `.completed`. The session ignores this method call if the current state is any value other than `.capturing`.

## See Also

### Controlling the session
- [func cancel()](./cancel%28%29.md)
  Requests that the capture session be canceled.
- [func pause()](./pause%28%29.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](./requestimagecapture%28%29.md)
  Requests a manual image capture.
- [func resume()](./resume%28%29.md)
  Resumes object tracking algorithms after [`pause()`](./pause%28%29.md) is called.
- [func startCapturing()](./startcapturing%28%29.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/finish())*