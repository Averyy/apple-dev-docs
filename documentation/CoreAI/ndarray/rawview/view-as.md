# view(as:)

**Framework**: Core AI  
**Kind**: method

Consume this raw view to create a typed view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
consuming func view<T>(as: T.Type = T.self) -> NDArray.View<T> where T : BitwiseCopyable
```

#### Discussion

> **Note**: `T` must match `self.scalarType.type`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/view(as:))*