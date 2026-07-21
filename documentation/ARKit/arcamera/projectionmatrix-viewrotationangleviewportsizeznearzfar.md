# projectionMatrix(viewRotationAngle:viewportSize:zNear:zFar:)

**Framework**: ARKit  
**Kind**: method

Creates a projection matrix for the camera given rendering parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func projectionMatrix(viewRotationAngle: CGFloat, viewportSize: CGSize, zNear: CGFloat, zFar: CGFloat) -> simd_float4x4
```

#### Return Value

The projection matrix for the given parameters.

#### Discussion

The projection matrix returned provides an aspect fill for the provided viewport size and view angle. If zFar is set to 0, an infinite projection matrix will be returned.

The view angle, in degrees, is the clockwise rotation needed to keep the camera image level with the horizon (`0` LandscapeRight, `90` Portrait, `180` LandscapeLeft, `270` PortraitUpsideDown). Obtain it from `ARSession.viewRotationAngle`.

## Parameters

- `viewRotationAngle`: View rotation angle in degrees.
- `viewportSize`: Viewport size.
- `zNear`: Near depth limit.
- `zFar`: Far depth limit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/projectionmatrix(viewrotationangle:viewportsize:znear:zfar:))*