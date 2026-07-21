# projectPoint(_:viewRotationAngle:viewportSize:)

**Framework**: ARKit  
**Kind**: method

Project a 3D point in world coordinate system into 2D viewport space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func projectPoint(_ point: simd_float3, viewRotationAngle: CGFloat, viewportSize: CGSize) -> CGPoint
```

#### Return Value

2D point in viewport coordinate system with origin at top-left.

#### Discussion

The view angle, in degrees, is the clockwise rotation needed to keep the camera image level with the horizon (`0` LandscapeRight, `90` Portrait, `180` LandscapeLeft, `270` PortraitUpsideDown). Obtain it from `ARSession.viewRotationAngle`.

## Parameters

- `point`: 3D point in world coordinate system.
- `viewRotationAngle`: View rotation angle in degrees.
- `viewportSize`: Viewport (or image) size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectpoint(_:viewrotationangle:viewportsize:))*