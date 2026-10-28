# NSSymbolAppearEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that makes the layers of a symbol-based image appear separately or as a whole.

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
@interface NSSymbolAppearEffect : NSSymbolEffect
```

## Overview

An appear transition causes a symbol to become visible using a scaling animation. You can choose to scale the image up or down and to animate the symbol by individual layers or as a whole.

## Topics

### Accessing symbol effects
- [+ appearDownEffect](./nssymbolappeareffect/appeardowneffect.md)
  An effect that makes the symbol scale down as it appears.
- [+ appearUpEffect](./nssymbolappeareffect/appearupeffect.md)
  An effect that makes the symbol scale up as it appears.
- [+ effect](./nssymbolappeareffect/effect.md)
  An animation that makes the layers of a symbol-based image appear separately or as a whole.
### Determining effect scope
- [- effectWithByLayer](./nssymbolappeareffect/effectwithbylayer.md)
  An effect that makes each layer appear separately.
- [- effectWithWholeSymbol](./nssymbolappeareffect/effectwithwholesymbol.md)
  An effect that makes all layers appear simultaneously.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)

## See Also

### Symbol effects
- [NSSymbolBounceEffect](./nssymbolbounceeffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [NSSymbolDisappearEffect](./nssymboldisappeareffect.md)
  A type that makes the layers of a symbol-based image disappear separately or as a whole.
- [NSSymbolPulseEffect](./nssymbolpulseeffect.md)
  A type that fades the opacity of some or all layers in a symbol-based image.
- [NSSymbolScaleEffect](./nssymbolscaleeffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [NSSymbolVariableColorEffect](./nssymbolvariablecoloreffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [NSSymbolBreatheEffect](./nssymbolbreatheeffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [NSSymbolRotateEffect](./nssymbolrotateeffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [NSSymbolWiggleEffect](./nssymbolwiggleeffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolappeareffect)*