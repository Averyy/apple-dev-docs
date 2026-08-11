# readIndices(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a Metal buffer containing the current contents of the index buffer for GPU read operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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

- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readindices(_:).md)
  Reads the current contents of the index buffer synchronously on the CPU.
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updateindices(_:).md)
  Updates the index buffer in place synchronously on the CPU.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replaceindices(_:).md)
  Replaces the entire contents of the index buffer synchronously on the CPU.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replaceindices(commandbuffer:).md)
  Returns a Metal buffer you populate on the GPU with the new contents of the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readindices(commandbuffer:))*