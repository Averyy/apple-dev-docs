# update(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the buffer synchronously on the CPU. The buffer is only valid for the lifetime of the callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func update<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer’s bytes for in-place modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/update(_:))*