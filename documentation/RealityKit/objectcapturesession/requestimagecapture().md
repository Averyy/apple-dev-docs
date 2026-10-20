# requestImageCapture()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Requests a manual image capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func requestImageCapture()
```

#### Discussion

If the session’s state is `.capturing`, call this method to request an image be manually captured at the current location. This function has no effect if the session is in any other state, or if [`canRequestImageCapture`](./canrequestimagecapture.md) is `false`.

## See Also

### Controlling the session
- [func cancel()](./cancel%28%29.md)
  Requests that the capture session be canceled.
- [func finish()](./finish%28%29.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](./pause%28%29.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func resume()](./resume%28%29.md)
  Resumes object tracking algorithms after [`pause()`](./pause%28%29.md) is called.
- [func startCapturing()](./startcapturing%28%29.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/requestimagecapture())*