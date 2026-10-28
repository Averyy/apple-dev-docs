# NSSymbolBounceEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.

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
@interface NSSymbolBounceEffect : NSSymbolEffect
```

## Overview

A bounce animation draws attention to a symbol by applying a brief scaling operation to the symbol’s layers. You can choose to scale the symbol up or down as it bounces.

```objc
// Add an effect in AppKit and UIKit.
// Bounce with a scale-up animation.
[self.imageView1 addSymbolEffect:NSSymbolBounceEffect.bounceUpEffect];

// Bounce three times with a scale-down animation.
NSSymbolEffectOptions *options = [NSSymbolEffectOptions optionsWithRepeatCount:3];
[self.imageView2 addSymbolEffect:NSSymbolBounceEffect.bounceDownEffect options:options];
```

## Topics

### Accessing symbol effects
- [+ bounceDownEffect](./nssymbolbounceeffect/bouncedowneffect.md)
  An effect that bounces the symbol downward.
- [+ bounceUpEffect](./nssymbolbounceeffect/bounceupeffect.md)
  An effect that bounces the symbol upward.
- [+ effect](./nssymbolbounceeffect/effect.md)
  An animation that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
### Determining effect scope
- [- effectWithByLayer](./nssymbolbounceeffect/effectwithbylayer.md)
  An effect that bounces each layer separately.
- [- effectWithWholeSymbol](./nssymbolbounceeffect/effectwithwholesymbol.md)
  An effect that bounces all layers simultaneously.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)

## See Also

### Symbol effects
- [NSSymbolAppearEffect](./nssymbolappeareffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
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

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolbounceeffect)*