# LowLevelDeformation.Renormalization

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An accessor for the renormalization buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Renormalization
```

## Topics

### Replacing geometry data
- [func replaceTriangleIndices<R>((inout MutableRawSpan) -> R) throws -> R](./renormalization-swift.struct/replacetriangleindices%28_%29.md)
  Fills the triangle index buffer using the given closure.
- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws -> R](./renormalization-swift.struct/replaceadjacencies%28_%29.md)
  Fills the adjacency buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws -> R](./renormalization-swift.struct/replaceadjacencyendindices%28_%29.md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.

## See Also

### Configuring deformation stages
- [var skinning: LowLevelDeformation.Skinning](./skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [LowLevelDeformation.Skinning](./skinning-swift.struct.md)
  An accessor for the skinning buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).
- [var blendShape: LowLevelDeformation.BlendShape](./blendshape-swift.property.md)
  The blend-shape data accessors for this deformation.
- [LowLevelDeformation.BlendShape](./blendshape-swift.struct.md)
  An accessor for the blend-shape buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).
- [var renormalization: LowLevelDeformation.Renormalization](./renormalization-swift.property.md)
  The renormalization data accessors for this deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct)*