# replaceIndices(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves a Metal index buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

A `MTLBuffer` ready for GPU write operations.

## Parameters

- `commandBuffer`: The command buffer writing to this buffer, or `nil` to skip synchronization.

## See Also

- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readindices(_:).md)
  Reads the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updateindices(_:).md)
  Updates the index buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replaceindices(_:).md)
  Replaces the index buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readindices(commandbuffer:).md)
  Retrieves the Metal index buffer for GPU reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/replaceindices(commandbuffer:))*