# read(_:)

**Framework**: RealityKit  
**Kind**: method

Reads the current transform data synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func read<R, E>(_ body: (consuming Span<float4x4>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a read-only span representing the transform data. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a read-only span over the transform data.

## See Also

- [func read(commandBuffer: (any MTLCommandBuffer)?) -> any MTLBuffer](lowlevelinstancetransformresource/read(commandbuffer:).md)
  Returns a Metal buffer containing the current transform data for GPU read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/read(_:))*