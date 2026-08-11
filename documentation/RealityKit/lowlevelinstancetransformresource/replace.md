# replace(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces all transform data synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func replace<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a mutable span representing the transform data. Upon entry the transform data is undefined; the closure is responsible for populating it with valid data. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the transform data and fully populates it.

## See Also

- [func replace(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/replace(commandbuffer:).md)
  Returns a Metal buffer you populate on the GPU with the new transform data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/replace(_:))*