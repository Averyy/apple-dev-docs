# replace(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves a Metal buffer for GPU replacement. The buffer’s contents are in an uninitialized state. The renderer waits for the command buffer to complete before using the buffer for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

A `MTLBuffer` ready for GPU write operations.

## Parameters

- `commandBuffer`: The command buffer writing to this buffer, or `nil` to skip synchronization.

## See Also

- [func replace<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/replace(_:).md)
  Replaces the buffer synchronously on the CPU. The buffer’s contents are unspecified; you must populate the buffer with valid data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/replace(commandbuffer:))*