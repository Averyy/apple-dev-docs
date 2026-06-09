# replace(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer’s bytes to fully populate.

## See Also

- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelbufferresource/replace(commandbuffer:).md)
  Retrieves a Metal buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/replace(_:))*