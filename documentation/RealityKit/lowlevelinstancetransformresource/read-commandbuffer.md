# read(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a Metal buffer containing the current transform data for GPU read operations.

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

A `MTLBuffer` ready for GPU read operations.

#### Discussion

The renderer waits for the provided command buffer to complete before discarding the buffer.

## Parameters

- `commandBuffer`: The command buffer that reads from this buffer, or `nil` to skip synchronization.

## See Also

- [func read<R, E>((consuming Span<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/read(_:).md)
  Reads the current transform data synchronously on the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/read(commandbuffer:))*