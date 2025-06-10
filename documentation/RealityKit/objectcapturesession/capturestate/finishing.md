# ObjectCaptureSession.CaptureState.finishing

**Framework**: RealityKit  
**Kind**: case

The session is saving outstanding data and finishing up.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
case finishing
```

#### Discussion

This state occurs  after your app calls [`finish()`](objectcapturesession/finish().md). The app should keep the session alive until it reaches `.completed` state to ensure all data has been saved.  The session will automatically move to `.completed` once all data is saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/capturestate/finishing)*