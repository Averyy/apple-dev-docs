# ReplaceSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A type that replaces the layers of one symbol-based image with those of another.

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
struct ReplaceSymbolEffect
```

#### Overview

A replace transition animates the change from one symbol image to another. You choose from one of the predefined scaling animations: Down-Up, Off-Up, and Up-Up.

## Topics

### Accessing symbol effects
- [var downUp: ReplaceSymbolEffect](replacesymboleffect/downup-swift.property.md)
  An effect that replaces a symbol by scaling it down, and scaling a different symbol up.
- [var offUp: ReplaceSymbolEffect](replacesymboleffect/offup-swift.property.md)
  An effect that replaces a symbol by removing it, and scaling a different symbol up.
- [var upUp: ReplaceSymbolEffect](replacesymboleffect/upup-swift.property.md)
  An effect that replaces a symbol by scaling it up, and scaling a different symbol up.
### Determining effect scope
- [var byLayer: ReplaceSymbolEffect](replacesymboleffect/bylayer.md)
  An effect that replaces each layer separately.
- [var wholeSymbol: ReplaceSymbolEffect](replacesymboleffect/wholesymbol.md)
  An effect that replaces all layers simultaneously.
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](replacesymboleffect/configuration.md)
  The configuration for the effect.
### Structures
- [ReplaceSymbolEffect.MagicReplace](replacesymboleffect/magicreplace.md)
  A symbol effect applies the MagicReplace animation to symbol images.
### Instance Methods
- [func magic(fallback: ReplaceSymbolEffect) -> ReplaceSymbolEffect.MagicReplace](replacesymboleffect/magic(fallback:).md)
  Returns an effect preferring MagicReplace and a configured ReplaceEffect if MagicReplace is not possible.
### Type Properties
- [static var downUp: ReplaceSymbolEffect](replacesymboleffect/downup-swift.type.property.md)
  Returns an effect requesting the Down-Up variant of the Replace animation.
- [static var offUp: ReplaceSymbolEffect](replacesymboleffect/offup-swift.type.property.md)
  Returns an effect requesting the Off-Up variant of the Replace animation.
- [static var upUp: ReplaceSymbolEffect](replacesymboleffect/upup-swift.type.property.md)
  Returns an effect requesting the Up-Up variant of the Replace animation.

## Relationships

### Conforms To
- [ContentTransitionSymbolEffect](contenttransitionsymboleffect.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct ScaleSymbolEffect](scalesymboleffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct BreatheSymbolEffect](breathesymboleffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [struct RotateSymbolEffect](rotatesymboleffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [struct WiggleSymbolEffect](wigglesymboleffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/replacesymboleffect)*