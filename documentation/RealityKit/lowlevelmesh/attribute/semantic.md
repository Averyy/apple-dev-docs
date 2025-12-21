# semantic

**Framework**: RealityKit  
**Kind**: property

The semantic of the vertex attribute, which describes how you want RealityKit to interpret the attribute.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var semantic: LowLevelMesh.VertexSemantic
```

#### Discussion

RealityKit consults the vertex semantic when interpreting the data in your [`LowLevelMesh`](lowlevelmesh.md). For example, an attribute with the semantic value of [`LowLevelMesh.VertexSemantic.position`](lowlevelmesh/vertexsemantic/position.md) uses to determine the position of a vertex.

## See Also

- [var format: MTLVertexFormat](lowlevelmesh/attribute/format.md)
  The format of the vertex attribute.
- [var offset: Int](lowlevelmesh/attribute/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var layoutIndex: Int](lowlevelmesh/attribute/layoutindex.md)
  The index of the layout that contains this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/attribute/semantic)*