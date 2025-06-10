# init(matrix:)

**Framework**: RealityKit  
**Kind**: init

Creates a new transform represented as a 4x4 matrix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(matrix: float4x4)
```

#### Discussion

A [`Transform`](transform.md) component can’t represent every transform that a general 4x4 matrix can . Using a 4x4 matrix during initialization might result in certain transformations, such as shear, being lost.

## Parameters

- `matrix`: A transformation matrix.

## See Also

- [init()](transform/init.md)
  Creates a transform with the values of the identity transform.
- [init(scale: SIMD3<Float>, rotation: simd_quatf, translation: SIMD3<Float>)](transform/init(scale:rotation:translation:).md)
  Creates a new transformation using the given values.
- [init(pitch: Float, yaw: Float, roll: Float)](transform/init(pitch:yaw:roll:).md)
  Creates a new transform from the specified Euler angles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/transform/init(matrix:))*