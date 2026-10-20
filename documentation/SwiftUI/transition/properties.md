# properties

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property  
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

## Default Implementations

### Transition Implementations
- [static var properties: TransitionProperties](./properties-3v8pe.md)
  Returns the properties this transition type has.

## See Also

### Configuring a transition
- [func animation(Animation?) -> some Transition](./animation%28_%29.md)
  Attaches an animation to this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transition/properties)*