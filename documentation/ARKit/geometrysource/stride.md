# stride

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The number of bytes between one vector and another in a geometry source’s buffer.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var stride: Int { get }
```

## See Also

### Inspecting geometry data
- [var buffer: any MTLBuffer](./buffer.md)
  A Metal buffer that contains per-vector data for a geometry source.
- [var count: Int](./count.md)
  The number of vectors in a geometry source.
- [var format: MTLVertexFormat](./format.md)
  The vertex format for data in a geometry source’s buffer.
- [var componentsPerVector: Int](./componentspervector.md)
  The number of scalar components in each vector in a geometry source.
- [var offset: Int](./offset.md)
  The offset, in bytes, from the beginning of a geometry source’s buffer.
- [var description: String](./description.md)
  A textual representation of this geometry source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/geometrysource/stride)*