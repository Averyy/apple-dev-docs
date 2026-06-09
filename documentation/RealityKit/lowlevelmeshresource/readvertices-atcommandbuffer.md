# readVertices(at:commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves a Metal vertex buffer for GPU reading.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func readVertices(at index: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

The underlying `MTLBuffer` for reading.

#### Discussion

The renderer waits for the command buffer to complete before discarding the buffer.

## Parameters

- `index`: The vertex buffer index to retrieve.
- `commandBuffer`: The command buffer using this buffer, or `nil` to skip synchronization.

## See Also

- [func readVertices<R, E>(at: Int, (RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readvertices(at:_:).md)
  Reads a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func updateVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updatevertices(at:_:).md)
  Updates a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replacevertices(at:_:).md)
  Replaces a vertex buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func replaceVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replacevertices(at:commandbuffer:).md)
  Retrieves a Metal vertex buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readvertices(at:commandbuffer:))*