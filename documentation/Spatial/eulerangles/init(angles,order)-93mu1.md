# init(angles:order:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a new Euler angles structure from the specified double-precision angles and order.

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
init(angles: simd_double3, order: __SPEulerAngleOrder)
```

#### Discussion

> **Note**: In Swift, use [EulerAngles.Order](./order-swift.typealias.md) in place of `__SPEulerAngleOrder`.

## Parameters

- `angles`: A three-element, double-precision vector that specifies the Euler angles.
- `order`: The Euler angle order.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Creates a new Euler angles structure.
- [init(angles: simd_float3, order: EulerAngles.Order)](./init%28angles,order%29-44rv1.md)
  Creates a new Euler angles structure from the specified single-precision angles and order.
- [init(x: Angle2D, y: Angle2D, z: Angle2D, order: EulerAngles.Order)](./init%28x,y,z,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](./init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/eulerangles/init(angles:order:)-93mu1)*