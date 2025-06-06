# pause()

**Framework**: RealityKit  
**Kind**: method

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

- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/pause())*