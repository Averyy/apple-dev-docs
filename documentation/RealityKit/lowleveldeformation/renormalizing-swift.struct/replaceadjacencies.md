# replaceAdjacencies(_:)

**Framework**: RealityKit  
**Kind**: method

Fills the adjacency buffer using the given closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func replaceAdjacencies<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R where R : ~Copyable
```

#### Return Value

The value returned by `body`.

#### Discussion

After the closure returns, the framework validates every entry against the triangle count. An out-of-range entry causes a throw.

> **Note**: If any entry is ≥ `renormalizing.indexCount / 3`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

- [func replaceTriangleIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replacetriangleindices(_:).md)
  Fills the triangle index buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/renormalizing-swift.struct/replaceadjacencyendindices(_:).md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalizing-swift.struct/replaceadjacencies(_:))*