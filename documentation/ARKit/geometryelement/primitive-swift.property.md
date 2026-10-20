# primitive

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Get the type of the geometry element.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var primitive: GeometryElement.Primitive { get }
```

## See Also

### Rendering geometry elements
- [var buffer: any MTLBuffer](./buffer.md)
  A Metal buffer that contains index data that defines the geometry of an object.
- [GeometryElement.Primitive](./primitive-swift.enum.md)
  The kind of primitive, lines or triangles, that a geometry element contains.
- [var count: Int](./count.md)
  The number of primitives in the Metal buffer for a geometry element.
- [var bytesPerIndex: Int](./bytesperindex.md)
  The number of bytes that represent an index value.
- [var description: String](./description.md)
  A textual representation of this geometry element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometryelement/primitive-swift.property)*