# removeSymbolEffect(ofType:options:animated:completion:)

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
@preconcurrency func removeSymbolEffect(ofType effect: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions = .default, animated: Bool = true, completion: UISymbolEffectCompletion? = nil)
```

## Parameters

- `effect`: The symbol effect to match for removal.
- `options`: The options to use when removing the symbol effect.
- `animated`: A Boolean value that indicates whether to animate the removal of a scale, appear, or disappear effect.
- `completion`: A completion handler the system calls after the removal is complete.

## See Also

### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./addsymboleffect%28_,options,animated,completion%29-18jqj.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./addsymboleffect%28_,options,animated,completion%29-2ixnm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./addsymboleffect%28_,options,animated,completion%29-896qd.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions, completion: UISymbolEffectCompletion?)](./setsymbolimage%28_,contenttransition,options,completion%29.md)
  Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./removesymboleffect%28oftype,options,animated,completion%29-218lh.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./removesymboleffect%28oftype,options,animated,completion%29-2boi2.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [typealias UISymbolEffectCompletion](../uisymboleffectcompletion-7qt7g.md)
  A completion handler for adding and removing symbol effects and transitions.
- [struct UISymbolEffectCompletionContext](../uisymboleffectcompletioncontext-swift.struct.md)
  Information about a symbol effect’s addition or removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/removesymboleffect(oftype:options:animated:completion:)-31zec)*