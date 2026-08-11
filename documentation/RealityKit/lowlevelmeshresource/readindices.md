# readIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Reads the current contents of the index buffer synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func readIndices<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a read-only span representing the contents of the index buffer. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the index buffer’s bytes.

## See Also

- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updateindices(_:).md)
  Updates the index buffer in place synchronously on the CPU.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replaceindices(_:).md)
  Replaces the entire contents of the index buffer synchronously on the CPU.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readindices(commandbuffer:).md)
  Returns a Metal buffer containing the current contents of the index buffer for GPU read operations.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replaceindices(commandbuffer:).md)
  Returns a Metal buffer you populate on the GPU with the new contents of the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readindices(_:))*