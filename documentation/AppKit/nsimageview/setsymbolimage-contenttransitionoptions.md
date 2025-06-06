# setSymbolImage(_:contentTransition:options:)

**Framework**: AppKit  
**Kind**: method

Sets a symbol image using the specified content-transition effect and options.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func setSymbolImage(_ image: NSImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default)
```

## Parameters

- `image`: The symbol image to set.
- `contentTransition`: The content transition to use when setting the symbol image.
- `options`: The options to use when setting the symbol image.

## See Also

- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/addsymboleffect(_:options:animated:)-4kete.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/addsymboleffect(_:options:animated:)-4p7p7.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/addsymboleffect(_:options:animated:)-66ckm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-8bszd.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-4c6vq.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool)](nsimageview/removesymboleffect(oftype:options:animated:)-8tk6g.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](nsimageview/removeallsymboleffects(options:animated:).md)
  Removes all symbol effects from the image view, using the specified options and animation setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/setsymbolimage(_:contenttransition:options:))*