# read(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Reads the current contents of the buffer resource synchronously on the CPU.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func read<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a read-only span representing the contents of the buffer resource. This span is valid only for the duration of the closure.

> **Throws**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the buffer’s bytes.

## See Also

### Reading buffer contents
- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](./read%28commandbuffer%29.md)
  Returns a Metal buffer containing the current contents of the buffer resource for GPU read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/read(_:))*