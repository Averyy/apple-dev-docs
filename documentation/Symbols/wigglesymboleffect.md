# WiggleSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A symbol effect that applies the Wiggle animation to symbol images.

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
struct WiggleSymbolEffect
```

#### Overview

The Wiggle animation applies a transitory translation or rotation effect to the symbol.

## Topics

### Instance Properties
- [var backward: WiggleSymbolEffect](wigglesymboleffect/backward.md)
  Returns a copy of the effect requesting an animation that moves back and forth horizontally based on the current locale, starting by moving backward.
- [var byLayer: WiggleSymbolEffect](wigglesymboleffect/bylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [var clockwise: WiggleSymbolEffect](wigglesymboleffect/clockwise.md)
  Returns a copy of the effect requesting an animation that rotates back and forth, starting by rotating clockwise.
- [var configuration: SymbolEffectConfiguration](wigglesymboleffect/configuration.md)
  The configuration for the effect.
- [var counterClockwise: WiggleSymbolEffect](wigglesymboleffect/counterclockwise.md)
  Returns a copy of the effect requesting an animation that rotates back and forth, starting by rotating counter-clockwise.
- [var down: WiggleSymbolEffect](wigglesymboleffect/down.md)
  Returns a copy of the effect requesting an animation that moves back and forth vertically, starting by moving down.
- [var forward: WiggleSymbolEffect](wigglesymboleffect/forward.md)
  Returns a copy of the effect requesting an animation that moves back and forth horizontally based on the current locale, starting by moving forward.
- [var left: WiggleSymbolEffect](wigglesymboleffect/left.md)
  Returns a copy of the effect requesting an animation that moves back and forth horizontally, starting by moving left.
- [var right: WiggleSymbolEffect](wigglesymboleffect/right.md)
  Returns a copy of the effect requesting an animation that moves back and forth horizontally, starting by moving right.
- [var up: WiggleSymbolEffect](wigglesymboleffect/up.md)
  Returns a copy of the effect requesting an animation that moves back and forth vertically, starting by moving up.
- [var wholeSymbol: WiggleSymbolEffect](wigglesymboleffect/wholesymbol.md)
  Returns a copy of the effect requesting an animation that applies to all motion groups simultaneously.
### Instance Methods
- [func custom(angle: Angle) -> WiggleSymbolEffect](wigglesymboleffect/custom(angle:)-1f09q.md)
- [func custom(angle: Double) -> WiggleSymbolEffect](wigglesymboleffect/custom(angle:)-cqpf.md)
  Returns a copy of the effect requesting an animation that moves back and forth along an axis with the passed in angle.

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
- [struct BreatheSymbolEffect](breathesymboleffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [struct RotateSymbolEffect](rotatesymboleffect.md)
  A symbol effect that applies the Rotate animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/wigglesymboleffect)*