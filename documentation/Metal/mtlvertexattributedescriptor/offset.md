# offset

**Framework**: Metal  
**Kind**: property

The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get set }
```

#### Discussion

The `offset` value must be a multiple of `4` bytes.

## See Also

- [var format: MTLVertexFormat](mtlvertexattributedescriptor/format.md)
  The format of the vertex attribute.
- [var bufferIndex: Int](mtlvertexattributedescriptor/bufferindex.md)
  The index in the argument table for the associated vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/offset)*