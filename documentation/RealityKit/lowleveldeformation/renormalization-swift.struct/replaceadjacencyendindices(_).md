# replaceAdjacencyEndIndices(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Fills the per-vertex adjacency end-indices buffer using the given closure.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func replaceAdjacencyEndIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws -> R where R : ~Copyable
```

## Return Value

The value returned by `body`.

## Discussion

After the closure returns, the framework validates every entry against the adjacency count. An out-of-range entry causes a throw.

> **Throws**: If any entry is greater than `renormalizing.adjacenciesCount`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

### Replacing geometry data
- [func replaceTriangleIndices<R>((inout MutableRawSpan) -> R) throws -> R](./replacetriangleindices%28_%29.md)
  Fills the triangle index buffer using the given closure.
- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws -> R](./replaceadjacencies%28_%29.md)
  Fills the adjacency buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct/replaceadjacencyendindices(_:))*