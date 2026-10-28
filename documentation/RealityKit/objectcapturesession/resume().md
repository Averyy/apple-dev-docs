# resume()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resumes object tracking algorithms after [`pause()`](./pause%28%29.md) is called.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func resume()
```

## Discussion

Call this method when the object capture view first appears on the screen, or after `pause()` is called to show another view temporarily.

## See Also

### Controlling the session
- [func cancel()](./cancel%28%29.md)
  Requests that the capture session be canceled.
- [func finish()](./finish%28%29.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](./pause%28%29.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](./requestimagecapture%28%29.md)
  Requests a manual image capture.
- [func startCapturing()](./startcapturing%28%29.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/resume())*