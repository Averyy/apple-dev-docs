# DrawOffSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A symbol effect that applies the DrawOff animation to symbol images.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DrawOffSymbolEffect
```

#### Overview

The DrawOff animation makes the symbol hidden either as a whole, or one motion group at a time, animating parts of the symbol with draw data.

## Topics

### Instance Properties
- [var byLayer: DrawOffSymbolEffect](drawoffsymboleffect/bylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [var configuration: SymbolEffectConfiguration](drawoffsymboleffect/configuration.md)
  The configuration for the effect.
- [var individually: DrawOffSymbolEffect](drawoffsymboleffect/individually.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group, where only one motion group is active at a time.
- [var nonReversed: DrawOffSymbolEffect](drawoffsymboleffect/nonreversed.md)
  Returns a copy of the effect requesting an animation that draws off following the draw metadata forwards.
- [var reversed: DrawOffSymbolEffect](drawoffsymboleffect/reversed.md)
  Returns a copy of the effect requesting an animation that draws off following the draw metadata in reverse.
- [var wholeSymbol: DrawOffSymbolEffect](drawoffsymboleffect/wholesymbol.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/drawoffsymboleffect)*