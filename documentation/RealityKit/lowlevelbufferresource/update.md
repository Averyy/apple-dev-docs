# update(_:)

**Framework**: RealityKit  
**Kind**: method

Updates the buffer resource in place synchronously on the CPU.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func update<R, E>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

You pass a closure that receives a mutable span representing the contents of the buffer resource, which the closure may modify. This span is valid only for the duration of the closure.

> **Note**: Any error thrown by `body`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer’s bytes for in-place modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferresource/update(_:))*