# ndArray

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

Waits for any pending write access on the underlying ndArray to complete, then returns it.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final var ndArray: NDArray? { get async throws }
```

## Discussion

> **Note**: If this value was constructed from a provided MTLBuffer directly, then this will return a copy of the data to avoid unsafe aliasing. If aliasing is desired, you can work with the original MTLBuffer directly.

Returns `nil` if `kind` is not `.ndArray`.

## See Also

### Accessing an async value
- [var kind: InferenceValue.Kind](./kind.md)
  The kind of inference value held by this async value.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](./pixelbuffer.md)
  Waits for any pending write access on the underlying pixel buffer to complete, then returns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/ndarray)*