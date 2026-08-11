# read(_:)

**Framework**: RealityKit  
**Kind**: method

Reads the current contents of the buffer resource synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a read-only span representing the contents of the buffer resource. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the buffer’s bytes.

## See Also

- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelbufferresource/read(commandbuffer:).md)
  Returns a Metal buffer containing the current contents of the buffer resource for GPU read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/read(_:))*