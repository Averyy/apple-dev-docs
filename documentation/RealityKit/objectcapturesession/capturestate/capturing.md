# ObjectCaptureSession.CaptureState.capturing

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

Auto-capture is in progress.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
case capturing
```

## Discussion

In this state the user is expected to orbit the device slowly and smoothly around the object in order to fully complete the capture dial.

In this state an app may also manually request captures with a call to [`requestImageCapture()`](../requestimagecapture%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/capturestate/capturing)*