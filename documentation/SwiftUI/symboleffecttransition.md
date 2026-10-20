# SymbolEffectTransition

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.

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
- [init<T>(effect: T, options: SymbolEffectOptions)](./symboleffecttransition/init%28effect,options%29.md)

## Relationships

### Conforms To
- [Transition](./transition.md)

## See Also

### Managing symbol effects
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](./view/symboleffect%28_,options,isactive%29.md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](./view/symboleffect%28_,options,value%29.md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](./view/symboleffectsremoved%28_%29.md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symboleffecttransition)*