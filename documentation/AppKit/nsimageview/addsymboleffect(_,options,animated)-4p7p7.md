# addSymbolEffect(_:options:animated:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a discrete symbol effect to the image view with the specified options and animation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func addSymbolEffect(_ effect: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true)
```

## Parameters

- `effect`: The symbol effect to add.
- `options`: The options for the symbol effect.
- `animated`: A Boolean value that indicates whether to animate the addition of a scale, appear, or disappear effect.

## See Also

### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./addsymboleffect%28_,options,animated%29-4kete.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./addsymboleffect%28_,options,animated%29-66ckm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(NSImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions)](./setsymbolimage%28_,contenttransition,options%29.md)
  Sets a symbol image using the specified content-transition effect and options.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-8bszd.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-4c6vq.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](./removesymboleffect%28oftype,options,animated%29-8tk6g.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/addsymboleffect(_:options:animated:)-4p7p7)*