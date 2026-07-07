# requestImageCapture()

**Framework**: RealityKit  
**Kind**: method

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

If the session’s state is `.capturing`, call this method to request an image be manually captured at the current location. This function has no effect if the session is in any other state, or if [`canRequestImageCapture`](objectcapturesession/canrequestimagecapture.md) is `false`.

## See Also

- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/requestimagecapture())*