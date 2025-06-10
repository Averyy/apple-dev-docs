# matrix

**Framework**: RealityKit  
**Kind**: property

The transform represented as a 4x4 matrix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var matrix: float4x4 { get set }
```

#### Discussion

The [`Transform`](transform.md) component can’t represent all transforms that a general 4x4 matrix can represent. Using a 4x4 matrix to set the transform is therefore a lossy event that might result in certain transformations, like shear, being dropped.

## See Also

- [var scale: SIMD3<Float>](transform/scale.md)
  The scaling factor applied to the entity.
- [var rotation: simd_quatf](transform/rotation.md)
  The rotation of the entity specified as a unit quaternion.
- [var translation: SIMD3<Float>](transform/translation.md)
  The position of the entity along the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/transform/matrix)*