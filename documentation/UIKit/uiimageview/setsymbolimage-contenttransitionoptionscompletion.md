# setSymbolImage(_:contentTransition:options:completion:)

**Framework**: UIKit  
**Kind**: method

Sets a symbol image using the specified content-transition effect, options, and completion handler.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setSymbolImage(_ image: UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, completion: UISymbolEffectCompletion? = nil)
```

## Parameters

- `image`: The symbol image to set.
- `contentTransition`: The content transition to use when setting the symbol image.
- `options`: The options to use when setting the symbol image.
- `completion`: A completion handler the system calls after setting the symbol image.

## See Also

- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-18jqj.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-2ixnm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/addsymboleffect(_:options:animated:completion:)-896qd.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-218lh.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-31zec.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](uiimageview/removesymboleffect(oftype:options:animated:completion:)-2boi2.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](uiimageview/removeallsymboleffects(options:animated:).md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [typealias UISymbolEffectCompletion](uisymboleffectcompletion-7qt7g.md)
  A completion handler for adding and removing symbol effects and transitions.
- [struct UISymbolEffectCompletionContext](uisymboleffectcompletioncontext-swift.struct.md)
  Information about a symbol effect’s addition or removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/setsymbolimage(_:contenttransition:options:completion:))*