# readVertices(at:_:)

**Framework**: RealityKit  
**Kind**: method

Reads the current contents of a vertex buffer synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func readVertices<R, E>(at index: Int, _ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a read-only span representing the contents of the vertex buffer. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `index`: The vertex buffer index to read.
- `body`: A closure that receives a read-only span over the buffer’s bytes.

## See Also

- [func updateVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/updatevertices(at:_:).md)
  Updates a vertex buffer in place synchronously on the CPU.
- [func replaceVertices<R, E>(at: Int, (inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelmeshresource/replacevertices(at:_:).md)
  Replaces the entire contents of a vertex buffer synchronously on the CPU.
- [func readVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/readvertices(at:commandbuffer:).md)
  Returns a Metal buffer containing the current contents of the vertex buffer for GPU read operations.
- [func replaceVertices(at: Int, commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelmeshresource/replacevertices(at:commandbuffer:).md)
  Returns a Metal buffer you populate on the GPU with the new contents of the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/readvertices(at:_:))*