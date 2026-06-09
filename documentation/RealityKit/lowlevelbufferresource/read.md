# read(_:)

**Framework**: RealityKit  
**Kind**: method

Reads the buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read<R, E>(_ body: (RawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the buffer’s bytes.

## See Also

- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelbufferresource/read(commandbuffer:).md)
  Retrieves the Metal buffer for GPU reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/read(_:))*