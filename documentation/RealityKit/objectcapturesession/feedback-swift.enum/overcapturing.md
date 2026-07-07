# ObjectCaptureSession.Feedback.overCapturing

**Framework**: RealityKit  
**Kind**: case

If the `numberOfShotsTaken > maximumNumberOfInputImages` then any additional shots will not be used in an on-device reconstruction and reconstruction is recommended to be done on a Mac that can support a greater number of images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
case overCapturing
```

#### Discussion

Note: this will only occur if `isOverCaptureEnabled` was set to true in the `Configuration` used to start the session – otherwise, the session will simply stop capturing once the device limit is reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/feedback-swift.enum/overcapturing)*