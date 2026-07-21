# pixelBuffer

**Framework**: Core AI  
**Kind**: property

Consume this value to access the underlying pixel buffer once any pending write is complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var pixelBuffer: CVMutablePixelBuffer? { get async throws }
```

#### Return Value

The underlying pixel buffer or `nil` if this was not an image value.

## See Also

- [var ndArray: NDArray?](inferencefunction/asyncmutablevalue/ndarray.md)
  Consume this value to access the underlying NDArray once any pending write is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/pixelbuffer)*