# vertexBufferCount

**Framework**: RealityKit  
**Kind**: property

The number of buffers this descriptor uses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var vertexBufferCount: Int { get }
```

#### Discussion

This value derives from the maximum `bufferIndex` each layout specifies in [`vertexLayouts`](lowlevelmesh/descriptor-swift.struct/vertexlayouts.md).

## See Also

- [var indexType: MTLIndexType](lowlevelmesh/descriptor-swift.struct/indextype.md)
  The data type of the indices that the index buffer stores.
- [var vertexAttributes: [LowLevelMesh.Attribute]](lowlevelmesh/descriptor-swift.struct/vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.
- [var vertexLayouts: [LowLevelMesh.Layout]](lowlevelmesh/descriptor-swift.struct/vertexlayouts.md)
  The list of layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/vertexbuffercount)*