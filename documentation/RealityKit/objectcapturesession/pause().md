# pause()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Pauses the automatic capture and other resource-intense algorithms.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func pause()
```

#### Discussion

Call this when object capture view is not visible, such as when a help screen is shown.

## See Also

### Controlling the session
- [func cancel()](./cancel%28%29.md)
  Requests that the capture session be canceled.
- [func finish()](./finish%28%29.md)
  Requests that the capture session be stopped and all data saved.
- [func requestImageCapture()](./requestimagecapture%28%29.md)
  Requests a manual image capture.
- [func resume()](./resume%28%29.md)
  Resumes object tracking algorithms after [`pause()`](./pause%28%29.md) is called.
- [func startCapturing()](./startcapturing%28%29.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/pause())*