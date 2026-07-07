# ndArray

**Framework**: Core AI  
**Kind**: property

Consume this value to access the underlying NDArray once any pending write is complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var ndArray: NDArray? { get async throws }
```

#### Return Value

The underlying ndArray or `nil` if this was not an ndArray value.

#### Discussion

> **Note**: If this value was constructed from a metal buffer directly, then the returned NDArray will be a copy of it. If aliasing is intended, you can work with the original metal buffer directly.

## See Also

- [var pixelBuffer: CVMutablePixelBuffer?](inferencefunction/asyncmutablevalue/pixelbuffer.md)
  Consume this value to access the underlying pixel buffer once any pending write is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/ndarray)*