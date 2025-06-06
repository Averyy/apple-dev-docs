# concat(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new modifier that is the result of concatenating `self` with `modifier`.

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
nonisolated
func concat<T>(_ modifier: T) -> ModifiedContent<Self, T>
```

## See Also

- [func animation(Animation?) -> some ViewModifier](viewmodifier/animation(_:).md)
  Returns a new version of the modifier that will apply `animation` to all animatable values within the modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewmodifier/concat(_:))*