# bounds

**Framework**: RealityKit  
**Kind**: property

The model-space bounding box of this part.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var bounds: BoundingBox
```

#### Discussion

RealityKit uses this bounding box for culling the mesh against the active camera.

Take care to maintain the bounds of each mesh part so that it completely contains the part’s geometry. Otherwise, RealityKit may not render your meshes correctly.

## See Also

- [var indexOffset: Int](lowlevelmesh/part/indexoffset.md)
  The offset, in bytes, of the first index.
- [var indexCount: Int](lowlevelmesh/part/indexcount.md)
  The number of indices to use for this part.
- [var topology: MTLPrimitiveType](lowlevelmesh/part/topology.md)
  The geometric primitive to use when rendering this part.
- [var materialIndex: Int](lowlevelmesh/part/materialindex.md)
  The material index this part associates with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/part/bounds)*