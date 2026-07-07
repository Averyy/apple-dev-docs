# setVertices(_:offset:semantic:)

**Framework**: RealityKit  
**Kind**: method

Binds a Metal buffer to the vertex attribute with the specified semantic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setVertices(_ buffer: any MTLBuffer, offset: Int, semantic: LowLevelDeformation.VertexSemantic) throws
```

#### Discussion

> **Note**: If the semantic is absent from the descriptor, if `offset` is out of bounds for `buffer`, or if the buffer is too small for the declared stride and vertex count.

## Parameters

- `buffer`: The Metal buffer containing the vertex data.
- `offset`: The byte offset into `buffer` where the vertex data begins.
- `semantic`: The vertex semantic of the attribute to bind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/mesh/setvertices(_:offset:semantic:))*