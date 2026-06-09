# init(bufferIndex:bufferOffset:bufferStride:stepFunction:stepRate:)

**Framework**: RealityKit  
**Kind**: init

Creates a layout with the given buffer index, offset, stride, step function, and step rate.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(bufferIndex: Int, bufferOffset: Int = 0, bufferStride: Int, stepFunction: MTLVertexStepFunction = .perVertex, stepRate: Int = 1)
```

## Parameters

- `bufferIndex`: The index of the buffer this layout refers to.
- `bufferOffset`: The byte offset into the buffer for the first byte of this layout. Defaults to `0`.
- `bufferStride`: The distance, in bytes, between consecutive vertices for attributes using this layout.
- `stepFunction`: How the vertex shader steps through this layout’s data. Defaults to `.perVertex`.
- `stepRate`: The number of instances that share the same per-instance data. Defaults to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/layout/init(bufferindex:bufferoffset:bufferstride:stepfunction:steprate:))*