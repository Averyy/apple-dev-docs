# DrawOnSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A symbol effect that applies the DrawOn animation to symbol images.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct DrawOnSymbolEffect
```

#### Overview

The DrawOn animation makes the symbol visible either as a whole, or one motion group at a time, animating parts of the symbol with draw data.

## Topics

### Instance Properties
- [var byLayer: DrawOnSymbolEffect](drawonsymboleffect/bylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [var configuration: SymbolEffectConfiguration](drawonsymboleffect/configuration.md)
  The configuration for the effect.
- [var individually: DrawOnSymbolEffect](drawonsymboleffect/individually.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group, where only one motion group is active at a time.
- [var wholeSymbol: DrawOnSymbolEffect](drawonsymboleffect/wholesymbol.md)
  Returns a copy of the effect requesting an animation that applies to all motion groups simultaneously.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IndefiniteSymbolEffect](indefinitesymboleffect.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SymbolEffect](symboleffect.md)
- [TransitionSymbolEffect](transitionsymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/drawonsymboleffect)*