# NSSymbolWiggleEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A symbol effect that applies the Wiggle animation to symbol images.

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
@interface NSSymbolWiggleEffect : NSSymbolEffect
```

#### Overview

The Wiggle animation applies a transitory translation or rotation effect to the symbol.

## Topics

### Instance Methods
- [- effectWithByLayer](./nssymbolwiggleeffect/effectwithbylayer.md)
  Returns a copy of the effect that animates incrementally, by layer.
- [- effectWithWholeSymbol](./nssymbolwiggleeffect/effectwithwholesymbol.md)
  Returns a copy of the effect that animates all layers of the symbol simultaneously.
### Type Methods
- [+ effect](./nssymbolwiggleeffect/effect.md)
  The default wiggle effect, determined by the system.
- [+ wiggleBackwardEffect](./nssymbolwiggleeffect/wigglebackwardeffect.md)
  Convenience initializer for a wiggle effect that moves back and forth horizontally based on the current locale, starting by moving backward.
- [+ wiggleClockwiseEffect](./nssymbolwiggleeffect/wiggleclockwiseeffect.md)
  Convenience initializer for a wiggle effect that rotates back and forth, starting by rotating clockwise.
- [+ wiggleCounterClockwiseEffect](./nssymbolwiggleeffect/wigglecounterclockwiseeffect.md)
  Convenience initializer for a wiggle effect that rotates back and forth, starting by rotating counter-clockwise.
- [+ wiggleCustomAngleEffect:](./nssymbolwiggleeffect/wigglecustomangleeffect_.md)
  Convenience initializer for a wiggle effect that moves back and forth along an axis, starting by moving toward a custom angle.
- [+ wiggleDownEffect](./nssymbolwiggleeffect/wiggledowneffect.md)
  Convenience initializer for a wiggle effect that moves back and forth vertically, starting by moving down.
- [+ wiggleForwardEffect](./nssymbolwiggleeffect/wiggleforwardeffect.md)
  Convenience initializer for a wiggle effect that moves back and forth horizontally based on the current locale, starting by moving forward.
- [+ wiggleLeftEffect](./nssymbolwiggleeffect/wigglelefteffect.md)
  Convenience initializer for a wiggle effect that moves back and forth horizontally, starting by moving left.
- [+ wiggleRightEffect](./nssymbolwiggleeffect/wigglerighteffect.md)
  Convenience initializer for a wiggle effect that moves back and forth horizontally, starting by moving right.
- [+ wiggleUpEffect](./nssymbolwiggleeffect/wiggleupeffect.md)
  Convenience initializer for a wiggle effect that moves back and forth vertically, starting by moving up.

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
- [NSSymbolBreatheEffect](./nssymbolbreatheeffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [NSSymbolRotateEffect](./nssymbolrotateeffect.md)
  A symbol effect that applies the Rotate animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolwiggleeffect)*