# readVertices(at:commandBuffer:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a Metal buffer containing the current contents of the vertex buffer for GPU read operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func readVertices(at index: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

## Return Value

A `MTLBuffer` ready for GPU read operations.

## Discussion

The renderer waits for the provided command buffer to complete before discarding the buffer.

## Parameters

- `index`: The vertex buffer index to read.
- `commandBuffer`: The command buffer that reads from this buffer, or `nil` to skip synchronization.

## See Also

### Accessing vertex data
- [func readVertices<R, E>(at: Int, (RawSpan) throws(E) -> R) throws(E) -> R](./readvertices%28at,_%29.md)
  Reads the current contents of a vertex buffer synchronously on the CPU.
- [func updateVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./updatevertices%28at,_%29.md)
  Updates a vertex buffer in place synchronously on the CPU.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./replacevertices%28at,_%29.md)
  Replaces the entire contents of a vertex buffer synchronously on the CPU.
- [func replaceVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](./replacevertices%28at,commandbuffer%29.md)
  Returns a Metal buffer you populate on the GPU with the new contents of the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readvertices(at:commandbuffer:))*