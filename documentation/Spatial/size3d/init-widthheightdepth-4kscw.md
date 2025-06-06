# init(width:height:depth:)

**Framework**: Spatial  
**Kind**: init

Creates a size structure from the specified floating-point values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<T>(width: T, height: T, depth: T) where T : BinaryFloatingPoint
```

## Parameters

- `width`: A floating-point value that specifies the width.
- `height`: A floating-point value that specifies the height.
- `depth`: A floating-point value that specifies the depth.

## See Also

- [init()](size3d/init.md)
  Creates a size structure.
- [init(width: Double, height: Double, depth: Double)](size3d/init(width:height:depth:)-4j9bk.md)
  Creates a size structure from the specified double-precision values.
- [init(simd_float3)](size3d/init(_:)-2ibhr.md)
  Creates a size structure from the specified single-precision vector.
- [init(simd_double3)](size3d/init(_:)-3y7nr.md)
  Creates a size structure from the specified double-precision vector.
- [init(vector: simd_double3)](size3d/init(vector:).md)
  Creates a size structure from the specified double-precision vector.
- [init(Point3D)](size3d/init(_:)-7kyp0.md)
  Creates a size structure from the specified Spatial point.
- [init(Vector3D)](size3d/init(_:)-6nss1.md)
  Creates a size structure from the specified Spatial vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3d/init(width:height:depth:)-4kscw)*