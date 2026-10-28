# viewRotationAngle

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The angle, in degrees, to rotate a view by so the `ARFrame` it displays stays level with the horizon as the device rotates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```objc
@property (atomic, readonly) CGFloat viewRotationAngle;
```

## Discussion

Updates in step with the system UI rotation. The value is normalized to `[0, 360)` (`0` at LandscapeRight, `90` at Portrait, `180` at LandscapeLeft, `270` at PortraitUpsideDown), or `NaN` until the angle is available (`viewLayer` is set and on screen).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/viewrotationangle-dmff)*