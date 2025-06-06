# worldTransform

**Framework**: PHASE  
**Kind**: property

A matrix, in scene coordinates, that determines the object’s pose in the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var worldTransform: simd_float4x4 { get set }
```

#### Discussion

The value of this property requires orthogonal basis vectors and uniform scale.

The framework interprets the transform’s position values in a right-handed coordinate system, where the  axis extends upward and and the negative  axis extends forward.

## See Also

- [var transform: simd_float4x4](phaseobject/transform.md)
  A matrix, in local coordinates, that determines the object’s pose in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/worldtransform)*