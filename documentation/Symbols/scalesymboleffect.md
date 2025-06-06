# ScaleSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A type that scales the layers in a symbol-based image separately or as a whole.

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
struct ScaleSymbolEffect
```

#### Overview

A scale animation draws attention to a symbol by changing the symbol’s scale indefinitely. You can choose to scale the symbol up or down.

## Topics

### Accessing symbol effects
- [var down: ScaleSymbolEffect](scalesymboleffect/down.md)
  An effect that scales the symbol down.
- [var up: ScaleSymbolEffect](scalesymboleffect/up.md)
  An effect that scales the symbol up.
### Determining effect scope
- [var byLayer: ScaleSymbolEffect](scalesymboleffect/bylayer.md)
  An effect that scales each layer separately.
- [var wholeSymbol: ScaleSymbolEffect](scalesymboleffect/wholesymbol.md)
  An effect that scales all layers simultaneously.
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](scalesymboleffect/configuration.md)
  The configuration for the effect.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IndefiniteSymbolEffect](indefinitesymboleffect.md)
- [Sendable](../Swift/Sendable.md)
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
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct BreatheSymbolEffect](breathesymboleffect.md)
- [struct RotateSymbolEffect](rotatesymboleffect.md)
- [struct WiggleSymbolEffect](wigglesymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/scalesymboleffect)*