# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an instance that type-erases `transition`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init<T>(_ transition: T) where T : Transition
```

## See Also

### Creating a custom transition
- [static func modifier<E>(active: E, identity: E) -> AnyTransition](./modifier%28active,identity%29.md)
  Returns a transition defined between an active modifier and an identity modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition/init(_:))*