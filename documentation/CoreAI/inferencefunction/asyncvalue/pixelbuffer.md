# pixelBuffer

**Framework**: Core AI  
**Kind**: property

Waits for any pending write access on the underlying pixel buffer to complete, then returns it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var pixelBuffer: CVReadOnlyPixelBuffer? { get async throws }
```

#### Discussion

Returns `nil` if `kind` is not `.image`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/pixelbuffer)*