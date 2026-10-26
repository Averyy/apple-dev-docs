# setSymbolImage:withContentTransition:options:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets a symbol image using the specified content-transition effect and options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setSymbolImage:(UIImage *) symbolImage withContentTransition:(NSSymbolContentTransition *) transition options:(NSSymbolEffectOptions *) options;
```

## Parameters

- `symbolImage`: The symbol image to set.
- `transition`: The content transition to use when setting the symbol image.
- `options`: The options to use when setting the symbol image.

## See Also

### Configuring symbol effects
- [var isSymbolAnimationEnabled: Bool](./issymbolanimationenabled.md)
  A Boolean value that indicates whether symbol effects animate.
- [- addSymbolEffect:](./addsymboleffect_.md)
  Adds a symbol effect to the bar button item with default options and animation.
- [- addSymbolEffect:options:](./addsymboleffect_options_.md)
  Adds a symbol effect to the bar button item with the specified options and default animation.
- [- addSymbolEffect:options:animated:](./addsymboleffect_options_animated_.md)
  Adds a symbol effect to the bar button item with the specified options and animation.
- [- setSymbolImage:withContentTransition:](./setsymbolimage_withcontenttransition_.md)
  Sets a symbol image using the specified content-transition effect.
- [- removeSymbolEffectOfType:](./removesymboleffectoftype_.md)
  Removes the symbol effect that matches the specified effect type.
- [- removeSymbolEffectOfType:options:](./removesymboleffectoftype_options_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options.
- [- removeSymbolEffectOfType:options:animated:](./removesymboleffectoftype_options_animated_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [- removeAllSymbolEffects](./removeallsymboleffects.md)
  Removes all symbol effects from the bar button item.
- [- removeAllSymbolEffectsWithOptions:](./removeallsymboleffectswithoptions_.md)
  Removes all symbol effects from the bar button item, using the specified options.
- [- removeAllSymbolEffectsWithOptions:animated:](./removeallsymboleffectswithoptions_animated_.md)
  Removes all symbol effects from the bar button item, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/setsymbolimage:withcontenttransition:options:)*