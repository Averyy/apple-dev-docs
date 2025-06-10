# DisappearSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A type that makes the layers of a symbol-based image disappear separately or as a whole.

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
struct DisappearSymbolEffect
```

#### Overview

A disappear transition causes a symbol to become invisible using a scaling animation. You can choose to scale the image up or down and to animate the symbol by individual layers or as a whole.

## Topics

### Accessing symbol effects
- [var down: DisappearSymbolEffect](disappearsymboleffect/down.md)
  An effect that scales the symbol down as it disappears.
- [var up: DisappearSymbolEffect](disappearsymboleffect/up.md)
  An effect that scales the symbol up as it disappears.
### Determining effect scope
- [var byLayer: DisappearSymbolEffect](disappearsymboleffect/bylayer.md)
  An effect that makes each layer disappear separately.
- [var wholeSymbol: DisappearSymbolEffect](disappearsymboleffect/wholesymbol.md)
  An effect that makes all layers disappear simultaneously.
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](disappearsymboleffect/configuration.md)
  The configuration for the effect.

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

## See Also

- [struct AppearSymbolEffect](appearsymboleffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
- [struct AutomaticSymbolEffect](automaticsymboleffect.md)
  A type that applies the default animation to a symbol-based image in a context-sensitive manner.
- [struct BounceSymbolEffect](bouncesymboleffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [struct PulseSymbolEffect](pulsesymboleffect.md)
  A type that fades the opacity of some or all layers in a symbol-based image.
- [struct ReplaceSymbolEffect](replacesymboleffect.md)
  A type that replaces the layers of one symbol-based image with those of another.
- [struct ScaleSymbolEffect](scalesymboleffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct BreatheSymbolEffect](breathesymboleffect.md)
- [struct RotateSymbolEffect](rotatesymboleffect.md)
- [struct WiggleSymbolEffect](wigglesymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/disappearsymboleffect)*