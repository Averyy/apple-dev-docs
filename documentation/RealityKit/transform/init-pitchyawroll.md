# init(pitch:yaw:roll:)

**Framework**: RealityKit  
**Kind**: init

Creates a new transform from the specified Euler angles.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(pitch x: Float = 0, yaw y: Float = 0, roll z: Float = 0)
```

#### Discussion

The rotation order using intrinsic rotation order is defined as:

1. Rotate around y-axis (yaw). 2. Rotate around the body-fixed x-axis (pitch). 3. Rotate around the body-fixed z-axis (roll).

The rotation order using extrinsic rotation order is defined as:

1. Rotate around the z-axis (roll). 2. Rotate around the world space x-axis (pitch). 3. Rotate around the world space y-axis (yaw).

## Parameters

- `x`: The rotation around the x-axis in radians.
- `y`: The rotation around the y-axis in radians.
- `z`: The rotation around the z-axis in radians.

## See Also

- [init()](transform/init.md)
  Creates a transform with the values of the identity transform.
- [init(scale: SIMD3<Float>, rotation: simd_quatf, translation: SIMD3<Float>)](transform/init(scale:rotation:translation:).md)
  Creates a new transformation using the given values.
- [init(matrix: float4x4)](transform/init(matrix:).md)
  Creates a new transform represented as a 4x4 matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/transform/init(pitch:yaw:roll:))*