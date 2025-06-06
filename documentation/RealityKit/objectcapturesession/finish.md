# finish()

**Framework**: RealityKit  
**Kind**: method

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

- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/finish())*