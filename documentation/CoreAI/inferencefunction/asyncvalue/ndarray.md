# ndArray

**Framework**: Core AI  
**Kind**: property

Waits for any pending write access on the underlying ndArray to complete, then returns it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var ndArray: NDArray? { get async throws }
```

#### Discussion

> **Note**: If this value was constructed from a provided MTLBuffer directly, then this will return a copy of the data to avoid unsafe aliasing. If aliasing is desired, you can work with the original MTLBuffer directly.

Returns `nil` if `kind` is not `.ndArray`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/ndarray)*