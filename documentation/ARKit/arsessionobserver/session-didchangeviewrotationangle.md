# session(_:didChangeViewRotationAngle:)

**Framework**: ARKit  
**Kind**: method

This is called when the view rotation angle changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
optional func session(_ session: ARSession, didChangeViewRotationAngle viewRotationAngle: CGFloat)
```

#### Discussion

ARKit calls this method when a new angle becomes available, in step with the system UI rotation. Implement it to rotate a view by the given angle so the `ARFrame` it displays stays level with the horizon as the device rotates.

## Parameters

- `session`: The session that provides the angle.
- `viewRotationAngle`: The angle, in degrees, normalized to `[0, 360)` (`0` at LandscapeRight, `90` at Portrait, `180` at LandscapeLeft, and `270` at PortraitUpsideDown).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didchangeviewrotationangle:))*