# modifier(active:identity:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns a transition defined between an active modifier and an identity modifier.

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
static func modifier<E>(active: E, identity: E) -> AnyTransition where E : ViewModifier
```

## See Also

### Creating a custom transition
- [init<T>(T)](./init%28_%29.md)
  Create an instance that type-erases `transition`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/modifier(active:identity:))*