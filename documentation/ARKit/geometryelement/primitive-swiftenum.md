# GeometryElement.Primitive

**Framework**: ARKit  
**Kind**: enum

The kind of primitive, lines or triangles, that a geometry element contains.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Primitive
```

## Topics

### Primitive shapes
- [GeometryElement.Primitive.line](geometryelement/primitive-swift.enum/line.md)
  Two vertices that connect to form a line.
- [GeometryElement.Primitive.triangle](geometryelement/primitive-swift.enum/triangle.md)
  Three vertices that connect to form a triangle.
### Inspecting geometry primitives
- [var indexCount: Int](geometryelement/primitive-swift.enum/indexcount.md)
  The number of indices for the `Primitive`.
### Instance Properties
- [var description: String](geometryelement/primitive-swift.enum/description.md)
  A textual representation of GeometryElement.Primitive

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var buffer: any MTLBuffer](geometryelement/buffer.md)
  A Metal buffer that contains index data that defines the geometry of an object.
- [var primitive: GeometryElement.Primitive](geometryelement/primitive-swift.property.md)
  Get the type of the geometry element.
- [var count: Int](geometryelement/count.md)
  The number of primitives in the Metal buffer for a geometry element.
- [var bytesPerIndex: Int](geometryelement/bytesperindex.md)
  The number of bytes that represent an index value.
- [var description: String](geometryelement/description.md)
  A textual representation of this geometry element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometryelement/primitive-swift.enum)*