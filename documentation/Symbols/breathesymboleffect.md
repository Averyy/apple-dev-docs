# BreatheSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A symbol effect that applies the Breathe animation to symbol images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct BreatheSymbolEffect
```

#### Overview

The Breathe animation smoothly scales a symbol up and down.

## Topics

### Instance Properties
- [var byLayer: BreatheSymbolEffect](breathesymboleffect/bylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [var configuration: SymbolEffectConfiguration](breathesymboleffect/configuration.md)
  The configuration for the effect.
- [var plain: BreatheSymbolEffect](breathesymboleffect/plain.md)
  Returns a copy of the effect requesting an animation that makes the symbol breathe with no additional styling.
- [var pulse: BreatheSymbolEffect](breathesymboleffect/pulse.md)
  Returns a copy of the effect requesting an animation that pulses layers as they breathe.
- [var wholeSymbol: BreatheSymbolEffect](breathesymboleffect/wholesymbol.md)
  Returns a copy of the effect requesting an animation that applies to all motion groups simultaneously.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiscreteSymbolEffect](discretesymboleffect.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IndefiniteSymbolEffect](indefinitesymboleffect.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SymbolEffect](symboleffect.md)

## See Also

- [struct AppearSymbolEffect](appearsymboleffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
- [struct AutomaticSymbolEffect](automaticsymboleffect.md)
  A type that applies the default animation to a symbol-based image in a context-sensitive manner.
- [struct BounceSymbolEffect](bouncesymboleffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [struct DisappearSymbolEffect](disappearsymboleffect.md)
  A type that makes the layers of a symbol-based image disappear separately or as a whole.
- [struct PulseSymbolEffect](pulsesymboleffect.md)
  A type that fades the opacity of some or all layers in a symbol-based image.
- [struct ReplaceSymbolEffect](replacesymboleffect.md)
  A type that replaces the layers of one symbol-based image with those of another.
- [struct ScaleSymbolEffect](scalesymboleffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct RotateSymbolEffect](rotatesymboleffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [struct WiggleSymbolEffect](wigglesymboleffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/breathesymboleffect)*