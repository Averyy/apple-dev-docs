# LowLevelDeformation.Renormalizing

**Framework**: RealityKit  
**Kind**: struct

An accessor for the renormalization buffers of a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Renormalizing
```

## Topics

### Replacing geometry data
- [func replaceTriangleIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replacetriangleindices(_:).md)
  Fills the triangle index buffer using the given closure.
- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replaceadjacencies(_:).md)
  Fills the adjacency buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replaceadjacencyendindices(_:).md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.

## See Also

- [var skinning: LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.struct.md)
  An accessor for the skinning buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var blending: LowLevelDeformation.Blending](lowleveldeformation/blending-swift.property.md)
  The blend-shape data accessors for this deformation.
- [LowLevelDeformation.Blending](lowleveldeformation/blending-swift.struct.md)
  An accessor for the blend-shape buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var renormalizing: LowLevelDeformation.Renormalizing](lowleveldeformation/renormalizing-swift.property.md)
  The renormalization data accessors for this deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalizing-swift.struct)*