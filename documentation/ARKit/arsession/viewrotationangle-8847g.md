# viewRotationAngle

**Framework**: ARKit  
**Kind**: property

The angle, in degrees, to rotate a view by so the `ARFrame` it displays stays level with the horizon as the device rotates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@nonobjc
var viewRotationAngle: CGFloat? { get }
```

#### Discussion

Updates in step with the system UI rotation. The value is normalized to `[0, 360)` (`0` at LandscapeRight, `90` at Portrait, `180` at LandscapeLeft, `270` at PortraitUpsideDown), or `nil` until the angle is available (`viewLayer` is set and on screen). Read it on demand; implement `session(_:didChangeViewRotationAngle:)` to react to changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/viewrotationangle-8847g)*