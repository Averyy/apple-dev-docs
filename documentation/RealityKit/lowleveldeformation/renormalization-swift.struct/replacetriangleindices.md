# replaceTriangleIndices(_:)

**Framework**: RealityKit  
**Kind**: method

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

#### Return Value

The value returned by `body`.

#### Discussion

After the closure returns, the framework validates every vertex index against the vertex count. An out-of-range index causes a throw.

> **Note**: If any vertex index is outside `[0, vertexCount)`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/renormalization-swift.struct/replacetriangleindices(_:))*