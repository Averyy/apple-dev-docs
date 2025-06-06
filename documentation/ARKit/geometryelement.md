# GeometryElement

**Framework**: ARKit  
**Kind**: struct

A container for vertex indices of lines or triangles.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct GeometryElement
```

## Topics

### Rendering geometry elements
- [var buffer: any MTLBuffer](geometryelement/buffer.md)
  A Metal buffer that contains index data that defines the geometry of an object.
- [var primitive: GeometryElement.Primitive](geometryelement/primitive-swift.property.md)
  Get the type of the geometry element.
- [GeometryElement.Primitive](geometryelement/primitive-swift.enum.md)
  The kind of primitive, lines or triangles, that a geometry element contains.
- [var count: Int](geometryelement/count.md)
  The number of primitives in the Metal buffer for a geometry element.
- [var bytesPerIndex: Int](geometryelement/bytesperindex.md)
  The number of bytes that represent an index value.
- [var description: String](geometryelement/description.md)
  A textual representation of this geometry element.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct GeometrySource](geometrysource.md)
  A container for geometrical vector data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometryelement)*