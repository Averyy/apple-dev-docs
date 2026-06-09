# read(_:)

**Framework**: RealityKit  
**Kind**: method

Provides read-only CPU access to the transform data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read<R, E>(_ body: (consuming Span<float4x4>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Parameters

- `body`: A closure that receives a `Span<float4x4>` over the current transform data. The span is valid only for the duration of the closure.

## See Also

- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/read(commandbuffer:).md)
  Returns a `MTLBuffer` for GPU-side read access to the transform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/read(_:))*