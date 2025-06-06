# startCapturing()

**Framework**: RealityKit  
**Kind**: method

Begins taking images for object capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func startCapturing()
```

#### Discussion

This call moves the session state from `.ready` or `.detecting` into `.capturing`. In object-centric scanning, this function is called after the user chooses the object selection bounding box and wishes to start the capture process. This call then moves the session state from `.detecting` into `.capturing`. In freeform scanning where the user skips the bounding box selection, this call moves the session state from `.ready` directly into `.capturing`.

## See Also

- [func cancel()](objectcapturesession/cancel.md)
  Requests that the capture session be canceled.
- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/startcapturing())*