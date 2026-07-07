# replace(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a `MTLBuffer` for GPU-side write access to the transform data.

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

An `MTLBuffer` containing the transform data.

#### Discussion

The renderer waits for `commandBuffer` to complete before reading from this buffer.

## Parameters

- `commandBuffer`: The command buffer writing to this buffer, or `nil` to skip synchronization.

## See Also

- [func replace<R, E>((inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/replace(_:).md)
  Provides full read-write CPU access, replacing all transform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/replace(commandbuffer:))*