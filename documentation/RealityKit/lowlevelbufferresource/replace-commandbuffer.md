# replace(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a Metal buffer you populate on the GPU with the new contents of the buffer resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

A `MTLBuffer` ready for GPU write operations.

#### Discussion

Upon return the buffer’s contents are undefined; the caller is responsible for populating it with valid data. The renderer waits for the provided command buffer to complete before using the buffer for rendering.

## Parameters

- `commandBuffer`: The command buffer that writes to this buffer, or `nil` to skip synchronization.

## See Also

- [func replace<R, E>((inout MutableRawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/replace(_:).md)
  Replaces the entire contents of the buffer resource synchronously on the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/replace(commandbuffer:))*