# resume()

**Framework**: RealityKit  
**Kind**: method

Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func resume()
```

#### Discussion

Call this method when the object capture view first appears on the screen, or after `pause()` is called to show another view temporarily.

## See Also

- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/resume())*