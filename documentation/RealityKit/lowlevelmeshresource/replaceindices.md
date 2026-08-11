# replaceIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the entire contents of the index buffer synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replaceIndices<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a mutable span representing the contents of the index buffer. Upon entry the buffer’s contents are undefined; the closure is responsible for populating it with valid data. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the index buffer’s bytes and fully populates it.

## See Also

- [func readIndices<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/readindices(_:).md)
  Reads the current contents of the index buffer synchronously on the CPU.
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updateindices(_:).md)
  Updates the index buffer in place synchronously on the CPU.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readindices(commandbuffer:).md)
  Returns a Metal buffer containing the current contents of the index buffer for GPU read operations.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replaceindices(commandbuffer:).md)
  Returns a Metal buffer you populate on the GPU with the new contents of the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/replaceindices(_:))*