# NSSymbolDisappearEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that makes the layers of a symbol-based image disappear separately or as a whole.

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
@interface NSSymbolDisappearEffect : NSSymbolEffect
```

#### Overview

A disappear transition causes a symbol to become invisible using a scaling animation. You can choose to scale the image up or down and to animate the symbol by individual layers or as a whole.

## Topics

### Accessing symbol effects
- [+ disappearDownEffect](./nssymboldisappeareffect/disappeardowneffect.md)
  An effect that scales the symbol down as it disappears.
- [+ disappearUpEffect](./nssymboldisappeareffect/disappearupeffect.md)
  An effect that scales the symbol up as it disappears.
- [+ effect](./nssymboldisappeareffect/effect.md)
  An animation that makes the layers of a symbol-based image disappear separately or as a whole.
### Determining effect scope
- [- effectWithByLayer](./nssymboldisappeareffect/effectwithbylayer.md)
  An effect that makes each layer disappear separately.
- [- effectWithWholeSymbol](./nssymboldisappeareffect/effectwithwholesymbol.md)
  An effect that makes all layers disappear simultaneously.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)

## See Also

### Symbol effects
- [NSSymbolAppearEffect](./nssymbolappeareffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
- [NSSymbolBounceEffect](./nssymbolbounceeffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
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

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboldisappeareffect)*