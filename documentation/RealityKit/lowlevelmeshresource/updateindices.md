# updateIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func updateIndices<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the index buffer’s bytes for in-place modification.

## See Also

- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readindices(_:).md)
  Reads the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replaceindices(_:).md)
  Replaces the index buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readindices(commandbuffer:).md)
  Retrieves the Metal index buffer for GPU reading.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replaceindices(commandbuffer:).md)
  Retrieves a Metal index buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/updateindices(_:))*