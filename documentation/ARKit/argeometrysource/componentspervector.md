# componentsPerVector

**Framework**: ARKit  
**Kind**: property

The number of scalar components in each vector.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var componentsPerVector: Int { get }
```

#### Discussion

In the case that [`componentsPerVector`](argeometrysource/componentspervector.md) is greater than 1, the element type of the geometry-source array is itself, a sequence.

## See Also

- [var count: Int](argeometrysource/count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](argeometrysource/format.md)
  The type of vector data in the buffer.
- [var offset: Int](argeometrysource/offset.md)
  The offset, in bytes, from the beginning of the buffer.
- [var stride: Int](argeometrysource/stride.md)
  The length, in bytes, of the start of one vector in the buffer to the start of the next vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/componentspervector)*