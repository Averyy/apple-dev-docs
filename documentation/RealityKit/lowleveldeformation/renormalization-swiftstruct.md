# LowLevelDeformation.Renormalization

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
struct Renormalization
```

## Topics

### Instance Methods
- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws -> R](lowleveldeformation/renormalization-swift.struct/replaceadjacencies(_:).md)
  Fills the adjacency buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws -> R](lowleveldeformation/renormalization-swift.struct/replaceadjacencyendindices(_:).md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.
- [func replaceTriangleIndices<R>((inout MutableRawSpan) -> R) throws -> R](lowleveldeformation/renormalization-swift.struct/replacetriangleindices(_:).md)
  Fills the triangle index buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct)*