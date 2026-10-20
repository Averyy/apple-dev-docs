# GeometryElement.Primitive

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The kind of primitive, lines or triangles, that a geometry element contains.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Primitive
```

## Topics

### Primitive shapes
- [GeometryElement.Primitive.line](./primitive-swift.enum/line.md)
  Two vertices that connect to form a line.
- [GeometryElement.Primitive.triangle](./primitive-swift.enum/triangle.md)
  Three vertices that connect to form a triangle.
### Inspecting geometry primitives
- [var indexCount: Int](./primitive-swift.enum/indexcount.md)
  The number of indices for the `Primitive`.
### Instance Properties
- [var description: String](./primitive-swift.enum/description.md)
  A textual representation of GeometryElement.Primitive

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Rendering geometry elements
- [var buffer: any MTLBuffer](./buffer.md)
  A Metal buffer that contains index data that defines the geometry of an object.
- [var primitive: GeometryElement.Primitive](./primitive-swift.property.md)
  Get the type of the geometry element.
- [var count: Int](./count.md)
  The number of primitives in the Metal buffer for a geometry element.
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes that represent an index value.
- [var description: String](./description.md)
  A textual representation of this geometry element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometryelement/primitive-swift.enum)*