# vertexLayouts

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The list of layouts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var vertexLayouts: [LowLevelMesh.Layout] { get set }
```

## Discussion

You assign a layout for each vertex attribute with [`layoutIndex`](../attribute/layoutindex.md).

## See Also

### Defining the descriptor’s contents
- [var indexType: MTLIndexType](./indextype.md)
  The data type of the indices that the index buffer stores.
- [var vertexAttributes: [LowLevelMesh.Attribute]](./vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.
- [var vertexBufferCount: Int](./vertexbuffercount.md)
  The number of buffers this descriptor uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/vertexlayouts)*