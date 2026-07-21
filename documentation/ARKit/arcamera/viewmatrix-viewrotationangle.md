# viewMatrix(viewRotationAngle:)

**Framework**: ARKit  
**Kind**: method

Returns the view matrix for the camera with a given view angle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func viewMatrix(viewRotationAngle: CGFloat) -> simd_float4x4
```

#### Return Value

The view matrix for the given view angle.

#### Discussion

The view matrix can be used to transform geometry from world space into camera space for a given view angle.

The view angle, in degrees, is the clockwise rotation needed to keep the camera image level with the horizon (`0` LandscapeRight, `90` Portrait, `180` LandscapeLeft, `270` PortraitUpsideDown). Obtain it from `ARSession.viewRotationAngle`.

## Parameters

- `viewRotationAngle`: The view rotation angle, in degrees, that will be used to render the camera’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/viewmatrix(viewrotationangle:))*