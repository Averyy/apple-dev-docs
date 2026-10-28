# cancel()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Requests that the capture session be canceled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
func cancel()
```

## Discussion

Call this when the user indicates they want to cancel the scan.  Calling this method eventually transitions the session to `.failed(Error)` Once the session enters the failed state  it is safe to tear down the session and create a new one if desired.

## See Also

### Controlling the session
- [func finish()](./finish%28%29.md)
  Requests that the capture session be stopped and all data saved.
- [func pause()](./pause%28%29.md)
  Pauses the automatic capture and other resource-intense algorithms.
- [func requestImageCapture()](./requestimagecapture%28%29.md)
  Requests a manual image capture.
- [func resume()](./resume%28%29.md)
  Resumes object tracking algorithms after [`pause()`](./pause%28%29.md) is called.
- [func startCapturing()](./startcapturing%28%29.md)
  Begins taking images for object capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/cancel())*