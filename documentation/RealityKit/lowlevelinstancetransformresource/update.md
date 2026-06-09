# update(_:)

**Framework**: RealityKit  
**Kind**: method

Provides partial read-write CPU access to the transform data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func update<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableSpan<float4x4>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

Use `update` when you want to modify a subset of transforms without fully replacing the buffer contents.

## Parameters

- `body`: A closure that receives a `MutableSpan<float4x4>` over the current transform data. The span is valid only for the duration of the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/update(_:))*