# replaceTriangleIndices(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Fills the triangle index buffer using the given closure.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func replaceTriangleIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws -> R where R : ~Copyable
```

## Return Value

The value returned by `body`.

## Discussion

After the closure returns, the framework validates every vertex index against the vertex count. An out-of-range index causes a throw.

> **Throws**: If any vertex index is outside `[0, vertexCount)`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

### Replacing geometry data
- [func replaceAdjacencies<R>((inout MutableRawSpan) -> R) throws -> R](./replaceadjacencies%28_%29.md)
  Fills the adjacency buffer using the given closure.
- [func replaceAdjacencyEndIndices<R>((inout MutableRawSpan) -> R) throws -> R](./replaceadjacencyendindices%28_%29.md)
  Fills the per-vertex adjacency end-indices buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct/replacetriangleindices(_:))*