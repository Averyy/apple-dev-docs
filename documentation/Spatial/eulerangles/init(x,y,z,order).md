# init(x:y:z:order:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a new Euler angles structure from the specified angle structures and order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
init(x: Angle2D, y: Angle2D, z: Angle2D, order: EulerAngles.Order)
```

## Parameters

- `x`: The first angle.
- `y`: The second angle.
- `z`: The third angle.
- `order`: The Euler angle order.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Creates a new Euler angles structure.
- [init(angles: simd_float3, order: EulerAngles.Order)](./init%28angles,order%29-44rv1.md)
  Creates a new Euler angles structure from the specified single-precision angles and order.
- [init(angles: simd_double3, order: __SPEulerAngleOrder)](./init%28angles,order%29-93mu1.md)
  Creates a new Euler angles structure from the specified double-precision angles and order.
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](./init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/eulerangles/init(x:y:z:order:))*