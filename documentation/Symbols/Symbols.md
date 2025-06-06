# Symbols

**Framework**: Symbols  
**Kind**: module

Apply universal animations to symbol-based images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

The Symbols framework provides access to symbol effects you can use to animate [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols) in your AppKit, UIKit, and SwiftUI apps. These animations exhibit different behaviors:

A symbol effect can exhibit multiple types of behavior. For instance, you can add a pulse effect with an option to occur a finite number of times — a discrete behavior. You can also add a pulse effect with an option to loop forever — an indefinite behavior.

```swift
// Add an effect in SwiftUI.
Image(systemName: "globe")
    // Add effect with discrete behavior to image view.
    .symbolEffect(.pulse, options: .repeat(3))

Image(systemName: "globe")
    // Add effect with indefinite behavior to image view.
    .symbolEffect(.pulse)
```

You can apply universal animation effects to symbol-based images that you display in image views. The Symbols framework provides a consistent set of effects to use regardless of your UI framework or langauge choices.

Consider a SwiftUI app that displays a variable color effect on a Wi-Fi symbol while the system searches for Wi-Fi networks.

```swift
// Add an effect in SwiftUI.
Image(systemName: "wifi")
    .symbolEffect(.variableColor.reversing)
```

Now consider an AppKit or UIKit version of the app. You can apply the same effect to animate the search for Wi-Fi networks.

## Topics

### Symbol effects
- [static var appear: AppearSymbolEffect](symboleffect/appear.md)
  An animation that makes the layers of a symbol-based image appear separately or as a whole.
- [static var bounce: BounceSymbolEffect](symboleffect/bounce.md)
  An animation that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [static var disappear: DisappearSymbolEffect](symboleffect/disappear.md)
  An animation that makes the layers of a symbol-based image disappear separately or as a whole.
- [static var pulse: PulseSymbolEffect](symboleffect/pulse.md)
  An animation that fades the opacity of some or all layers in a symbol-based image.
- [static var scale: ScaleSymbolEffect](symboleffect/scale.md)
  An animation that scales the layers in a symbol-based image separately or as a whole.
- [static var variableColor: VariableColorSymbolEffect](symboleffect/variablecolor.md)
  An animation that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
### Symbol content transitions
- [static var replace: ReplaceSymbolEffect](symboleffect/replace.md)
  An animation that replaces the layers of one symbol-based image with those of another.
- [static var automatic: AutomaticSymbolEffect](symboleffect/automatic.md)
  A transition that applies the default animation to a symbol-based image in a context-sensitive manner.
### Symbol effect types
- [struct AppearSymbolEffect](appearsymboleffect.md)
  A type that makes the layers of a symbol-based image appear separately or as a whole.
- [struct AutomaticSymbolEffect](automaticsymboleffect.md)
  A type that applies the default animation to a symbol-based image in a context-sensitive manner.
- [struct BounceSymbolEffect](bouncesymboleffect.md)
  A type that applies a transitory scaling effect, or bounce, to the layers in a symbol-based image separately or as a whole.
- [struct DisappearSymbolEffect](disappearsymboleffect.md)
  A type that makes the layers of a symbol-based image disappear separately or as a whole.
- [struct PulseSymbolEffect](pulsesymboleffect.md)
  A type that fades the opacity of some or all layers in a symbol-based image.
- [struct ReplaceSymbolEffect](replacesymboleffect.md)
  A type that replaces the layers of one symbol-based image with those of another.
- [struct ScaleSymbolEffect](scalesymboleffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct BreatheSymbolEffect](breathesymboleffect.md)
- [struct RotateSymbolEffect](rotatesymboleffect.md)
- [struct WiggleSymbolEffect](wigglesymboleffect.md)
### Symbol effect options
- [struct SymbolEffectOptions](symboleffectoptions.md)
  Options that configure how effects apply to symbol-based images.
### Symbol effect protocols
- [protocol SymbolEffect](symboleffect.md)
  A presentation effect that you apply to a symbol-based image.
- [protocol DiscreteSymbolEffect](discretesymboleffect.md)
  An effect that performs a transient animation.
- [protocol IndefiniteSymbolEffect](indefinitesymboleffect.md)
  An animation that continually affects a symbol until it’s disabled or removed.
- [protocol ContentTransitionSymbolEffect](contenttransitionsymboleffect.md)
  An effect that animates between symbols or different configurations of the same symbol.
- [protocol TransitionSymbolEffect](transitionsymboleffect.md)
  An effect that animates a symbol in or out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Symbols)*