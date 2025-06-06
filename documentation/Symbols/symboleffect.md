# SymbolEffect

**Framework**: Symbols  
**Kind**: protocol

A presentation effect that you apply to a symbol-based image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol SymbolEffect : Hashable, Sendable
```

## Topics

### Effects
- [static var appear: AppearSymbolEffect](symboleffect/appear.md)
  An animation that makes the layers of a symbol-based image appear separately or as a whole.
- [static var bounce: BounceSymbolEffect](symboleffect/bounce.md)
  An animation that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [static var disappear: DisappearSymbolEffect](symboleffect/disappear.md)
  An animation that makes the layers of a symbol-based image disappear separately or as a whole.
- [static var pulse: PulseSymbolEffect](symboleffect/pulse.md)
  An animation that fades the opacity of some or all layers in a symbol-based image.
- [static var scale: ScaleSymbolEffect](symboleffect/scale.md)
  An animation that scales the layers in a symbol-based image separately or as a whole.
- [static var variableColor: VariableColorSymbolEffect](symboleffect/variablecolor.md)
  An animation that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [static var breathe: BreatheSymbolEffect](symboleffect/breathe.md)
- [static var rotate: RotateSymbolEffect](symboleffect/rotate.md)
- [static var wiggle: WiggleSymbolEffect](symboleffect/wiggle.md)
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](symboleffect/configuration.md)
  A configuration for a symbol effect.
- [struct SymbolEffectConfiguration](symboleffectconfiguration.md)
  A type that specifies the configuration of a symbol effect.
### Type Properties
- [static var automatic: AutomaticSymbolEffect](symboleffect/automatic.md)
  A transition that applies the default animation to a symbol-based image in a context-sensitive manner.
- [static var replace: ReplaceSymbolEffect](symboleffect/replace.md)
  An animation that replaces the layers of one symbol-based image with those of another.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [AppearSymbolEffect](appearsymboleffect.md)
- [AutomaticSymbolEffect](automaticsymboleffect.md)
- [BounceSymbolEffect](bouncesymboleffect.md)
- [BreatheSymbolEffect](breathesymboleffect.md)
- [DisappearSymbolEffect](disappearsymboleffect.md)
- [PulseSymbolEffect](pulsesymboleffect.md)
- [ReplaceSymbolEffect](replacesymboleffect.md)
- [ReplaceSymbolEffect.MagicReplace](replacesymboleffect/magicreplace.md)
- [RotateSymbolEffect](rotatesymboleffect.md)
- [ScaleSymbolEffect](scalesymboleffect.md)
- [VariableColorSymbolEffect](variablecolorsymboleffect.md)
- [WiggleSymbolEffect](wigglesymboleffect.md)

## See Also

- [protocol DiscreteSymbolEffect](discretesymboleffect.md)
  An effect that performs a transient animation.
- [protocol IndefiniteSymbolEffect](indefinitesymboleffect.md)
  An animation that continually affects a symbol until it’s disabled or removed.
- [protocol ContentTransitionSymbolEffect](contenttransitionsymboleffect.md)
  An effect that animates between symbols or different configurations of the same symbol.
- [protocol TransitionSymbolEffect](transitionsymboleffect.md)
  An effect that animates a symbol in or out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffect)*