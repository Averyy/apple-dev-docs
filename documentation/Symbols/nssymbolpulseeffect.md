# NSSymbolPulseEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that fades the opacity of some or all layers in a symbol-based image.

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
@interface NSSymbolPulseEffect : NSSymbolEffect
```

#### Overview

A pulse animation applies an opacity ramp to the layers in a symbol. You can choose to animate only layers marked as “always-pulses” or all layers simultaneously. Participating layers reduce their opacity to a minimum value before returning to fully opaque.

```objc
// Add an effect in AppKit and UIKit.
// Pulse only layers marked as "always-pulse."
NSSymbolEffectOptions *options = [NSSymbolEffectOptions optionsWithNonRepeating];
[self.imageView1 addSymbolEffect:NSSymbolPulseEffect.effect options: options];

// Pulse all layers three times simultaneously.
NSSymbolEffectOptions *options = [NSSymbolEffectOptions optionsWithRepeatCount:3];
[self.imageView2 addSymbolEffect:[NSSymbolPulseEffect.effect effectWithWholeSymbol] options:options];
```

## Topics

### Accessing symbol effects
- [+ effect](./nssymbolpulseeffect/effect.md)
  The default pulse effect, determined by the system.
### Determining effect scope
- [- effectWithByLayer](./nssymbolpulseeffect/effectwithbylayer.md)
  A copy of the effect requesting an animation that pulses only the layers marked to always pulse.
- [- effectWithWholeSymbol](./nssymbolpulseeffect/effectwithwholesymbol.md)
  A copy of the effect requesting an animation that pulses all layers simultaneously.

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

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolpulseeffect)*