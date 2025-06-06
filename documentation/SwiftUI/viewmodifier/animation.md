# animation(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func animation(_ animation: Animation?) -> some ViewModifier
```

## See Also

- [func concat<T>(T) -> ModifiedContent<Self, T>](viewmodifier/concat(_:).md)
  Returns a new modifier that is the result of concatenating `self` with `modifier`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewmodifier/animation(_:))*