# init(x:y:z:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a rotation axis from the specified floating-point values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init<T>(x: T, y: T, z: T) where T : BinaryFloatingPoint
```

## Parameters

- `x`: A floating-point value that specifies the x-coordinate value.
- `y`: A floating-point value that specifies the y-coordinate value.
- `z`: A floating-point value that specifies the z-coordinate value.

## See Also

### Creating a 3D rotation axis structure
- [init()](./init%28%29.md)
  Creates a rotation axis.
- [init(simd_float3)](./init%28_%29-96si4.md)
  Creates a rotation axis from the specified single-precision vector.
- [init(simd_double3)](./init%28_%29-804sx.md)
  Creates a rotation axis from the specified double-precision vector.
- [init(vector: simd_double3)](./init%28vector%29.md)
  Creates a rotation axis from a three-element double-precision vector.
- [init(Vector3D)](./init%28_%29-2zdal.md)
  Creates a rotation axis from a Spatial vector.
- [init(x: Double, y: Double, z: Double)](./init%28x,y,z%29-3z5nm.md)
  Creates a rotation axis from the specified double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotationaxis3d/init(x:y:z:)-1x93q)*