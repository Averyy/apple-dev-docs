# updateVertices(at:_:)

**Framework**: RealityKit  
**Kind**: method

Updates a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func updateVertices<R, E>(at index: Int, _ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: Any error thrown by `body`.

## Parameters

- `index`: The vertex buffer index to update.
- `body`: A closure that receives a mutable span over the buffer’s bytes for in-place modification.

## See Also

- [func readVertices<R, E>(at: Int, (RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readvertices(at:_:).md)
  Reads a vertex buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replacevertices(at:_:).md)
  Replaces a vertex buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func readVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readvertices(at:commandbuffer:).md)
  Retrieves a Metal vertex buffer for GPU reading.
- [func replaceVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replacevertices(at:commandbuffer:).md)
  Retrieves a Metal vertex buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/updatevertices(at:_:))*