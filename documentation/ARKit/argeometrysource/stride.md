# stride

**Framework**: ARKit  
**Kind**: property

The length, in bytes, of the start of one vector in the buffer to the start of the next vector.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var stride: Int { get }
```

#### Discussion

Stride may contain padding, so it’s not always equal to the vector-format’s total size in bytes.

## See Also

- [var componentsPerVector: Int](argeometrysource/componentspervector.md)
  The number of scalar components in each vector.
- [var count: Int](argeometrysource/count.md)
  The number of vectors in the buffer.
- [var format: MTLVertexFormat](argeometrysource/format.md)
  The type of vector data in the buffer.
- [var offset: Int](argeometrysource/offset.md)
  The offset, in bytes, from the beginning of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/stride)*