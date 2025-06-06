# properties

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

Returns the properties this transition type has.

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
@MainActor
@preconcurrency static var properties: TransitionProperties { get }
```

#### Discussion

Defaults to `TransitionProperties()`.

## See Also

- [func animation(Animation?) -> some Transition](transition/animation(_:).md)
  Attaches an animation to this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transition/properties)*