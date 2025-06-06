# removeAllSymbolEffects(options:animated:)

**Framework**: UIKit  
**Kind**: method

Removes all symbol effects from the bar button item, using the specified options and animation setting.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func removeAllSymbolEffects(options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `options`: The options to use when removing the symbol effects.
- `animated`: A Boolean value that indicates whether to animate the removal of a scale, appear, or disappear effects.

## See Also

- [var isSymbolAnimationEnabled: Bool](uibarbuttonitem/issymbolanimationenabled.md)
  A Boolean value that indicates whether symbol effects animate.
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-3iew0.md)
  Adds an indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-6jx3e.md)
  Adds a discrete, indefinite symbol effect to the bar button item with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/addsymboleffect(_:options:animated:)-9dytr.md)
  Adds a discrete symbol effect to the bar button item with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](uibarbuttonitem/setsymbolimage(_:contenttransition:options:).md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-214pl.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-7m567.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](uibarbuttonitem/removesymboleffect(oftype:options:animated:)-8zc4d.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/removeallsymboleffects(options:animated:))*