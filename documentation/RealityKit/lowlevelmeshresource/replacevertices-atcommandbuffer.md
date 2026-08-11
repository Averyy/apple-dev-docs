# replaceVertices(at:commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a Metal buffer you populate on the GPU with the new contents of the vertex buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replaceVertices(at index: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

A `MTLBuffer` ready for GPU write operations.

#### Discussion

Upon return the buffer’s contents are undefined; the caller is responsible for populating it with valid data. The renderer waits for the provided command buffer to complete before using the buffer for rendering.

## Parameters

- `index`: The vertex buffer index to replace.
- `commandBuffer`: The command buffer that writes to this buffer, or `nil` to skip synchronization.

## See Also

- [func readVertices<R, E>(at: Int, (RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readvertices(at:_:).md)
  Reads the current contents of a vertex buffer synchronously on the CPU.
- [func updateVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updatevertices(at:_:).md)
  Updates a vertex buffer in place synchronously on the CPU.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replacevertices(at:_:).md)
  Replaces the entire contents of a vertex buffer synchronously on the CPU.
- [func readVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readvertices(at:commandbuffer:).md)
  Returns a Metal buffer containing the current contents of the vertex buffer for GPU read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/replacevertices(at:commandbuffer:))*