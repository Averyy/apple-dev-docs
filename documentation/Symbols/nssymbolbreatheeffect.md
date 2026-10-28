# NSSymbolBreatheEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A symbol effect that applies the Breathe animation to symbol images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@interface NSSymbolBreatheEffect : NSSymbolEffect
```

## Overview

The Breathe animation smoothly scales a symbol up and down.

## Topics

### Instance Methods
- [- effectWithByLayer](./nssymbolbreatheeffect/effectwithbylayer.md)
  Returns a copy of the effect that animates incrementally, by layer.
- [- effectWithWholeSymbol](./nssymbolbreatheeffect/effectwithwholesymbol.md)
  Returns a copy of the effect that animates all layers of the symbol simultaneously.
### Type Methods
- [+ breathePlainEffect](./nssymbolbreatheeffect/breatheplaineffect.md)
  Convenience initializer for a breathe effect that makes the symbol breathe with no other styling.
- [+ breathePulseEffect](./nssymbolbreatheeffect/breathepulseeffect.md)
  Convenience initializer for a breathe effect that pulses layers as they breathe.
- [+ effect](./nssymbolbreatheeffect/effect.md)
  The default breathe effect, determined by the system.

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
- [NSSymbolScaleEffect](./nssymbolscaleeffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [NSSymbolVariableColorEffect](./nssymbolvariablecoloreffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [NSSymbolRotateEffect](./nssymbolrotateeffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [NSSymbolWiggleEffect](./nssymbolwiggleeffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolbreatheeffect)*