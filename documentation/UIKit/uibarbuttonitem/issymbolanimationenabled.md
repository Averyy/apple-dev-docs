# isSymbolAnimationEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether symbol effects animate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isSymbolAnimationEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isSymbolAnimationEnabled) BOOL symbolAnimationEnabled;
```

## See Also

### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./addsymboleffect%28_,options,animated%29-3iew0.md)
  Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./addsymboleffect%28_,options,animated%29-6jx3e.md)
  Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./addsymboleffect%28_,options,animated%29-9dytr.md)
  Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](./setsymbolimage%28_,contenttransition,options%29.md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-214pl.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-7m567.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-8zc4d.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the bar button item, using the specified options and animation setting.
- [- addSymbolEffect:](./addsymboleffect_.md)
  Adds a symbol effect to the bar button item with default options and animation.
- [- addSymbolEffect:options:](./addsymboleffect_options_.md)
  Adds a symbol effect to the bar button item with the specified options and default animation.
- [- addSymbolEffect:options:animated:](./addsymboleffect_options_animated_.md)
  Adds a symbol effect to the bar button item with the specified options and animation.
- [- setSymbolImage:withContentTransition:](./setsymbolimage_withcontenttransition_.md)
  Sets a symbol image using the specified content-transition effect.
- [- setSymbolImage:withContentTransition:options:](./setsymbolimage_withcontenttransition_options_.md)
  Sets a symbol image using the specified content-transition effect and options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/issymbolanimationenabled)*