# view(as:)

**Framework**: Core AI  
**Kind**: method

Consume this raw view to create a typed view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
consuming func view<T>(as: T.Type = T.self) -> NDArray.View<T> where T : BitwiseCopyable
```

#### Discussion

> **Note**: `T` must match `self.scalarType.type`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/view(as:))*