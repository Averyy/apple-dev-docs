# replaceTriangleIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Fills the triangle index buffer using the given closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func replaceTriangleIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R where R : ~Copyable
```

#### Return Value

The value returned by `body`.

#### Discussion

After the closure returns, the framework validates every vertex index against the vertex count. An out-of-range index causes a throw.

> **Note**: If any vertex index is outside `[0, vertexCount)`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replaceadjacencies(_:).md)
  Fills the adjacency buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replaceadjacencyendindices(_:).md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalizing-swift.struct/replacetriangleindices(_:))*