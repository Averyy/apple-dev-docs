# replace(_:)

**Framework**: RealityKit  
**Kind**: method

Provides full read-write CPU access, replacing all transform data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Parameters

- `body`: A closure that receives a `MutableSpan<float4x4>` for the new transform data. The span is valid only for the duration of the closure.

## See Also

- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/replace(commandbuffer:).md)
  Returns a `MTLBuffer` for GPU-side write access to the transform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/replace(_:))*