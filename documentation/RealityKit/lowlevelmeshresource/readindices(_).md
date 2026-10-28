# readIndices(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Reads the current contents of the index buffer synchronously on the CPU.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func readIndices<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Discussion

You pass a closure that receives a read-only span representing the contents of the index buffer. This span is valid only for the duration of the closure.

> **Throws**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the index buffer’s bytes.

## See Also

### Accessing index data
- [func updateIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./updateindices%28_%29.md)
  Updates the index buffer in place synchronously on the CPU.
- [func replaceIndices<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](./replaceindices%28_%29.md)
  Replaces the entire contents of the index buffer synchronously on the CPU.
- [func readIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](./readindices%28commandbuffer%29.md)
  Returns a Metal buffer containing the current contents of the index buffer for GPU read operations.
- [func replaceIndices(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](./replaceindices%28commandbuffer%29.md)
  Returns a Metal buffer you populate on the GPU with the new contents of the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readindices(_:))*