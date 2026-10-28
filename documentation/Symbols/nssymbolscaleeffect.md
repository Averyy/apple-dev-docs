# NSSymbolScaleEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that scales the layers in a symbol-based image separately or as a whole.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface NSSymbolScaleEffect : NSSymbolEffect
```

## Overview

A scale animation draws attention to a symbol by changing the symbol’s scale indefinitely. You can choose to scale the symbol up or down.

## Topics

### Accessing symbol effects
- [+ effect](./nssymbolscaleeffect/effect.md)
  An animation that scales the layers in a symbol-based image separately or as a whole.
- [+ scaleDownEffect](./nssymbolscaleeffect/scaledowneffect.md)
  An effect that scales the symbol down.
- [+ scaleUpEffect](./nssymbolscaleeffect/scaleupeffect.md)
  An effect that scales the symbol up.
### Determining effect scope
- [- effectWithByLayer](./nssymbolscaleeffect/effectwithbylayer.md)
  An effect that scales each layer separately.
- [- effectWithWholeSymbol](./nssymbolscaleeffect/effectwithwholesymbol.md)
  An effect that scales all layers simultaneously.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)

## See Also

### Symbol effects
- [NSSymbolAppearEffect](./nssymbolappeareffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
- [NSSymbolBounceEffect](./nssymbolbounceeffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [NSSymbolDisappearEffect](./nssymboldisappeareffect.md)
  A type that makes the layers of a symbol-based image disappear separately or as a whole.
- [NSSymbolPulseEffect](./nssymbolpulseeffect.md)
  A type that fades the opacity of some or all layers in a symbol-based image.
- [NSSymbolVariableColorEffect](./nssymbolvariablecoloreffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [NSSymbolBreatheEffect](./nssymbolbreatheeffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [NSSymbolRotateEffect](./nssymbolrotateeffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [NSSymbolWiggleEffect](./nssymbolwiggleeffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolscaleeffect)*