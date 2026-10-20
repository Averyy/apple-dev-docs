# eulerAngles(order:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a rotation’s Euler angles.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles
```

```c
static SPEulerAngles SPRotation3DGetEulerAngles(SPRotation3D rotation, SPEulerAngleOrder order);
```

#### Return Value

A structure that represents Euler angles and ordering.

#### Discussion

> **Note**: In Swift, use [EulerAngles.Order](../eulerangles/order-swift.typealias.md) in place of `__SPEulerAngleOrder`.

## Parameters

- `order`: The Euler angle ordering.

## See Also

### Inspecting a 3D rotation’s properties
- [var angle: Angle2D](./angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](./axis.md)
  The axis of the rotation.
- [struct EulerAngles](../eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](./quaternion.md)
  A quaternion that represents the rotation.
- [var vector: simd_double4](./vector.md)
  The underlying vector of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/eulerangles(order:))*