# replaceAdjacencyEndIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Fills the per-vertex adjacency end-indices buffer using the given closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func replaceAdjacencyEndIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws -> R where R : ~Copyable
```

#### Return Value

The value returned by `body`.

#### Discussion

After the closure returns, the framework validates every entry against the adjacency count. An out-of-range entry causes a throw.

> **Note**: If any entry is greater than `renormalizing.adjacenciesCount`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct/replaceadjacencyendindices(_:))*