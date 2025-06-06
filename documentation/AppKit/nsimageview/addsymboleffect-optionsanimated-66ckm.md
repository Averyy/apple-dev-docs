# addSymbolEffect(_:options:animated:)

**Framework**: AppKit  
**Kind**: method

Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func addSymbolEffect(_ effect: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `effect`: The symbol effect to add.
- `options`: The options for the symbol effect.
- `animated`: A Boolean value that indicates whether to animate the addition of a scale, appear, or disappear effect.

## See Also

- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/addsymboleffect(_:options:animated:)-4kete.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/addsymboleffect(_:options:animated:)-4p7p7.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(NSImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](nsimageview/setsymbolimage(_:contenttransition:options:).md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-8bszd.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-4c6vq.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-8tk6g.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](nsimageview/removeallsymboleffects(options:animated:).md)
  Removes all symbol effects from the image view, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/addsymboleffect(_:options:animated:)-66ckm)*