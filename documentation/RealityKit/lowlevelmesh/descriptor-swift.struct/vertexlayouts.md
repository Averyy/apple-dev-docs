# vertexLayouts

**Framework**: RealityKit  
**Kind**: property

The list of layouts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var vertexLayouts: [LowLevelMesh.Layout] { get set }
```

#### Discussion

You assign a layout for each vertex attribute with [`layoutIndex`](lowlevelmesh/attribute/layoutindex.md).

## See Also

- [var indexType: MTLIndexType](lowlevelmesh/descriptor-swift.struct/indextype.md)
  The data type of the indices that the index buffer stores.
- [var vertexAttributes: [LowLevelMesh.Attribute]](lowlevelmesh/descriptor-swift.struct/vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.
- [var vertexBufferCount: Int](lowlevelmesh/descriptor-swift.struct/vertexbuffercount.md)
  The number of buffers this descriptor uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/vertexlayouts)*