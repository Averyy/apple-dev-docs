# offset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger offset;
```

## Discussion

Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Organizing the vertex attribute
- [var format: MTLVertexFormat](./format.md)
  The format of the vertex attribute.
- [var bufferIndex: Int](./bufferindex.md)
  The index in the argument table for the associated vertex buffer.
- [enum MTLVertexFormat](../mtlvertexformat.md)
  The vertex data format options for render pipelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/offset)*