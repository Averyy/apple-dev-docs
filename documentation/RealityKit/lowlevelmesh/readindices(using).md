# readIndices(using:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the Metal index buffer for GPU reading.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func readIndices(using commandBuffer: any MTLCommandBuffer) -> any MTLBuffer
```

## Parameters

- `commandBuffer`: The [`MTLCommandBuffer`](../../Metal/mtlcommandbuffer.md) you intend to use for reading. RealityKit waits for the command buffer to complete before discarding the buffer.

## See Also

### Accessing mesh data on the GPU with Metal
- [func read(bufferIndex: Int, using: any MTLCommandBuffer) -> any MTLBuffer](./read%28bufferindex,using%29.md)
  Retrieves a Metal vertex buffer at the specified index, for GPU reading.
- [func replace(bufferIndex: Int, using: any MTLCommandBuffer) -> any MTLBuffer](./replace%28bufferindex,using%29.md)
  Retrieves a Metal vertex buffer you can use to replace the contents of the specified buffer on the GPU using Metal.
- [func replaceIndices(using: any MTLCommandBuffer) -> any MTLBuffer](./replaceindices%28using%29.md)
  Retrieves a Metal index buffer that you can use to replace the indices of this low-level mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/readindices(using:))*