# NSSymbolVariableColorEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.

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
@interface NSSymbolVariableColorEffect : NSSymbolEffect
```

#### Overview

A variable color animation draws attention to a symbol by changing the opacity of the symbol’s layers. You can choose to apply the effect to layers either cumulatively or iteratively. For cumulative animations, each layer’s opacity remains changed until the end of the animation cycle. For iterative animations, each layer’s opacity changes briefly before returning to its original state.

> **Note**:  Variable color animations affect only symbols containing variable color layers.

```objc
// Add an effect in AppKit and UIKit.
// Iteratively activates layers.
NSSymbolEffectOptions *options = [NSSymbolEffectOptions optionsWithRepeatCount:1];
[self.imageView1 addSymbolEffect:[NSSymbolVariableColorEffect.effect effectWithIterative] options: options];

// Cumulatively activates layers reversing and repeating three times.
NSSymbolEffectOptions *options = [NSSymbolEffectOptions optionsWithRepeatCount:3];
NSSymbolVariableColorEffect *effect =
    [[NSSymbolVariableColorEffect.effect effectWithHideInactiveLayers] effectWithReversing];
[self.imageView2 addSymbolEffect:effect options:options];
```

## Topics

### Accessing symbol effects
- [+ effect](./nssymbolvariablecoloreffect/effect.md)
  An animation that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
### Controlling fill style
- [- effectWithCumulative](./nssymbolvariablecoloreffect/effectwithcumulative.md)
  An effect that enables each layer of a symbol-based image in sequence.
- [- effectWithIterative](./nssymbolvariablecoloreffect/effectwithiterative.md)
  An effect that momentarily enables each layer of a symbol-based image in sequence.
### Changing playback style
- [- effectWithNonReversing](./nssymbolvariablecoloreffect/effectwithnonreversing.md)
  An effect that doesn’t reverse each time it repeats.
- [- effectWithReversing](./nssymbolvariablecoloreffect/effectwithreversing.md)
  An effect that reverses each time it repeats.
### Affecting inactive layers
- [- effectWithDimInactiveLayers](./nssymbolvariablecoloreffect/effectwithdiminactivelayers.md)
  An effect that dims inactive layers in a symbol-based image.
- [- effectWithHideInactiveLayers](./nssymbolvariablecoloreffect/effectwithhideinactivelayers.md)
  An effect that hides inactive layers in a symbol-based image.

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
- [NSSymbolBreatheEffect](./nssymbolbreatheeffect.md)
  A symbol effect that applies the Breathe animation to symbol images.
- [NSSymbolRotateEffect](./nssymbolrotateeffect.md)
  A symbol effect that applies the Rotate animation to symbol images.
- [NSSymbolWiggleEffect](./nssymbolwiggleeffect.md)
  A symbol effect that applies the Wiggle animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolvariablecoloreffect)*