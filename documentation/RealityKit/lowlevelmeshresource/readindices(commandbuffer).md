# readIndices(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a Metal buffer containing the current contents of the index buffer for GPU read operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

A `MTLBuffer` ready for GPU read operations.

#### Discussion

The renderer waits for the provided command buffer to complete before discarding the buffer.

## Parameters

- `commandBuffer`: The command buffer that reads from this buffer, or `nil` to skip synchronization.

## See Also

### Accessing index data
- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](./readindices%28_%29.md)
  Reads the current contents of the index buffer synchronously on the CPU.
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./updateindices%28_%29.md)
  Updates the index buffer in place synchronously on the CPU.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./replaceindices%28_%29.md)
  Replaces the entire contents of the index buffer synchronously on the CPU.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](./replaceindices%28commandbuffer%29.md)
  Returns a Metal buffer you populate on the GPU with the new contents of the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readindices(commandbuffer:))*