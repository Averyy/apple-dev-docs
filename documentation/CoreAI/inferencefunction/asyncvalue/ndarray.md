# ndArray

**Framework**: Core AI  
**Kind**: property

Waits for any pending write access on the underlying ndArray to complete, then returns it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final var ndArray: NDArray? { get async throws }
```

#### Discussion

> **Note**: If this value was constructed from a provided MTLBuffer directly, then this will return a copy of the data to avoid unsafe aliasing. If aliasing is desired, you can work with the original MTLBuffer directly.

Returns `nil` if `kind` is not `.ndArray`.

## See Also

- [var kind: InferenceValue.Kind](inferencefunction/asyncvalue/kind.md)
  The kind of inference value held by this async value.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](inferencefunction/asyncvalue/pixelbuffer.md)
  Waits for any pending write access on the underlying pixel buffer to complete, then returns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/ndarray)*