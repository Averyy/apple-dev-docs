# layoutIndex

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The index of the layout that contains this attribute.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var layoutIndex: Int
```

## Discussion

The index refers to an entry in [`vertexLayouts`](../descriptor-swift.struct/vertexlayouts.md).

## See Also

### Describing an attribute
- [var format: MTLVertexFormat](./format.md)
  The format of the vertex attribute.
- [var offset: Int](./offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var semantic: LowLevelMesh.VertexSemantic](./semantic.md)
  The semantic of the vertex attribute, which describes how you want RealityKit to interpret the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/attribute/layoutindex)*