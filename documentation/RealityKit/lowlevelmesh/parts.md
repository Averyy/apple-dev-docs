# parts

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A mutable collection of parts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var parts: LowLevelMesh.PartsCollection { get set }
```

## Discussion

The parts of a [`LowLevelMesh`](../lowlevelmesh.md) object specify how to interpret the index buffer. You can also use `parts` to customize the material index and primitive type.

## See Also

### Describing a low-level mesh
- [let descriptor: LowLevelMesh.Descriptor](./descriptor-swift.property.md)
  The definition of the structure of this low-level mesh.
- [var indexCapacity: Int](./indexcapacity.md)
  The capacity of the index buffer, measured in indices.
- [var vertexCapacity: Int](./vertexcapacity.md)
  The capacity of the vertex buffer, measured in vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/parts)*