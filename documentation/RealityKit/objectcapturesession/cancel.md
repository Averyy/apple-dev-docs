# cancel()

**Framework**: RealityKit  
**Kind**: method

Requests that the capture session be canceled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func cancel()
```

#### Discussion

Call this when the user indicates they want to cancel the scan.  Calling this method eventually transitions the session to `.failed(Error)` Once the session enters the failed state  it is safe to tear down the session and create a new one if desired.

## See Also

- [func finish()](objectcapturesession/finish.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](objectcapturesession/pause.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](objectcapturesession/requestimagecapture.md)
  Requests a manual image capture.
- [func resume()](objectcapturesession/resume.md)
  Resumes object tracking algorithms after [`pause()`](objectcapturesession/pause().md) is called.
- [func startCapturing()](objectcapturesession/startcapturing.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/cancel())*