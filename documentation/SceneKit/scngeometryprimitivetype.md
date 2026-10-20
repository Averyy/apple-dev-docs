# SCNGeometryPrimitiveType

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

The drawing primitive that connects vertices when rendering a geometry element, used by the [`primitiveType`](./scngeometryelement/primitivetype.md) property to specify how SceneKit interprets the geometry element’s data.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNGeometryPrimitiveType
```

```c
enum SCNGeometryPrimitiveType : NSInteger;
```

## Topics

### Constants
- [SCNGeometryPrimitiveType.triangles](./scngeometryprimitivetype/triangles.md)
  The geometry element’s data is a sequence of triangles, with each triangle described by three new vertices.
- [SCNGeometryPrimitiveType.triangleStrip](./scngeometryprimitivetype/trianglestrip.md)
  The geometry element’s data is a sequence of triangles, with each triangle described by one new vertex and two vertices from the previous triangle.
- [SCNGeometryPrimitiveType.line](./scngeometryprimitivetype/line.md)
  The geometry element’s data is a sequence of line segments, with each line segment described by two new vertices.
- [SCNGeometryPrimitiveType.point](./scngeometryprimitivetype/point.md)
  The geometry element’s data is a sequence of unconnected points.
### Enumeration Cases
- [SCNGeometryPrimitiveType.polygon](./scngeometryprimitivetype/polygon.md)
### Initializers
- [init?(rawValue: Int)](./scngeometryprimitivetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Indexes
- [var data: Data](./scngeometryelement/data.md)
  The data describing the geometry element.
- [var bytesPerIndex: Int](./scngeometryelement/bytesperindex.md)
  The number of bytes that represent each index value in the element’s data.
- [var primitiveType: SCNGeometryPrimitiveType](./scngeometryelement/primitivetype.md)
  The drawing primitive that connects vertices when rendering the geometry element.
- [var primitiveCount: Int](./scngeometryelement/primitivecount.md)
  The number of primitives in the element.
- [var primitiveRange: NSRange](./scngeometryelement/primitiverange.md)
  The range of primitives from the geometry element to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryprimitivetype)*