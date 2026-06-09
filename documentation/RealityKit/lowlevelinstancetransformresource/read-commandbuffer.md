# read(commandBuffer:)

**Framework**: RealityKit  
**Kind**: method

Returns a `MTLBuffer` for GPU-side read access to the transform data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer
```

#### Return Value

An `MTLBuffer` containing the current transform data.

## Parameters

- `commandBuffer`: The command buffer using this buffer, or `nil` to skip synchronization.

## See Also

- [func read<R, E>((consuming Span<float4x4>) throws(E) -> R) throws(E) -> R](lowlevelinstancetransformresource/read(_:).md)
  Provides read-only CPU access to the transform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/read(commandbuffer:))*