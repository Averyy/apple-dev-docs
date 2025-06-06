# SymbolEffectTransition

**Framework**: SwiftUI  
**Kind**: struct

Creates a transition that applies the Appear or Disappear symbol animation to symbol images within the inserted or removed view hierarchy.

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
@frozen @preconcurrency struct SymbolEffectTransition
```

#### Overview

Other views are unaffected by this transition.

## Topics

### Creating a transition
- [init<T>(effect: T, options: SymbolEffectOptions)](symboleffecttransition/init(effect:options:).md)

## Relationships

### Conforms To
- [Transition](transition.md)

## See Also

- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](view/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](view/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](view/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symboleffecttransition)*