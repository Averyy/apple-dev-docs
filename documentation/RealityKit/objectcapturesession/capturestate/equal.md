# ==(_:_:)

**Framework**: RealityKit  
**Kind**: op

Two states are defined equal if they have the same case.  Specifically, a `.failed(Error)` state will match any other failed state regardless of the actual error payload.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
static func == (lhs: ObjectCaptureSession.CaptureState, rhs: ObjectCaptureSession.CaptureState) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/capturestate/==(_:_:))*