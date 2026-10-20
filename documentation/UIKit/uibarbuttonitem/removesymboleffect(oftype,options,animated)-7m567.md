# removeSymbolEffect(ofType:options:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func removeSymbolEffect(ofType effect: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `effect`: The symbol effect to match for removal.
- `options`: The options to use when removing the symbol effect.
- `animated`: A Boolean value that indicates whether to animate the removal of a scale, appear, or disappear effect.

## See Also

### Configuring symbol effects
- [var isSymbolAnimationEnabled: Bool](./issymbolanimationenabled.md)
  A Boolean value that indicates whether symbol effects animate.
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
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-8zc4d.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the bar button item, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/removesymboleffect(oftype:options:animated:)-7m567)*