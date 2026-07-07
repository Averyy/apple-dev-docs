# read(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Retrieves the Metal buffer for GPU reading.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

The underlying `MTLBuffer` for reading.

#### Discussion

The renderer waits for the command buffer to complete before discarding the buffer.

## Parameters

- `commandBuffer`: The command buffer using this buffer, or `nil` to skip synchronization.

## See Also

- [func read<R, E>((RawSpan) throws(E) -> R) throws(E) -> R](lowlevelbufferresource/read(_:).md)
  Reads the buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/read(commandbuffer:))*