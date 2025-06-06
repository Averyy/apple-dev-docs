# VariableColorSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct VariableColorSymbolEffect
```

#### Overview

A variable color animation draws attention to a symbol by changing the opacity of the symbol’s layers. You can choose to apply the effect to layers either cumulatively or iteratively. For cumulative animations, each layer’s opacity remains changed until the end of the animation cycle. For iterative animations, each layer’s opacity changes briefly before returning to its original state.

> **Note**:  Variable color animations affect only symbols containing variable color layers.

> ❗ **Important**:  Because SwiftUI is a state-driven framework, you pass a `value` parameter when adding discrete effects, like bounce. You trigger the animation by changing the `value` parameter. Because AppKit and UIKit are event-driven frameworks, discrete effects animate automatically when added to an image view.

```swift
// Add an effect in SwiftUI.
@State private var value1 = 0
@State private var value2 = 0
var body: some View {
    HStack {
        Image(systemName: "cellularbars")
            // Iteratively activates layers.
            .symbolEffect(.variableColor.iterative, value: value1)
            .onTapGesture {
                value1 += 1
            }
        Image(systemName: "cellularbars")
            // Cumulatively activates layers reversing and repeating three times.
            .symbolEffect(.variableColor.hideInactiveLayers.reversing, options: .repeat(3), value: value2)
            .onTapGesture {
                value2 += 1
            }
    }
}
```

```swift
// Add an effect in AppKit and UIKit.
// Iteratively activates layers.
imageView1.addSymbolEffect(.variableColor.iterative, options: .nonRepeating)
    
// Cumulatively activates layers reversing and repeating three times.
imageView2.addSymbolEffect(.variableColor.hideInactiveLayers.cumulative, options: .repeat(3))
```

## Topics

### Controlling fill style
- [var cumulative: VariableColorSymbolEffect](variablecolorsymboleffect/cumulative.md)
  An effect that enables each layer of a symbol-based image in sequence.
- [var iterative: VariableColorSymbolEffect](variablecolorsymboleffect/iterative.md)
  An effect that momentarily enables each layer of a symbol-based image in sequence.
### Changing playback style
- [var nonReversing: VariableColorSymbolEffect](variablecolorsymboleffect/nonreversing.md)
  An effect that doesn’t reverse each time it repeats.
- [var reversing: VariableColorSymbolEffect](variablecolorsymboleffect/reversing.md)
  An effect that reverses each time it repeats.
### Affecting inactive layers
- [var dimInactiveLayers: VariableColorSymbolEffect](variablecolorsymboleffect/diminactivelayers.md)
  An effect that dims inactive layers in a symbol-based image.
- [var hideInactiveLayers: VariableColorSymbolEffect](variablecolorsymboleffect/hideinactivelayers.md)
  An effect that hides inactive layers in a symbol-based image.
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](variablecolorsymboleffect/configuration.md)
  The configuration for the effect.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiscreteSymbolEffect](discretesymboleffect.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IndefiniteSymbolEffect](indefinitesymboleffect.md)
- [Sendable](../Swift/Sendable.md)
- [SymbolEffect](symboleffect.md)

## See Also

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
- [struct BreatheSymbolEffect](breathesymboleffect.md)
- [struct RotateSymbolEffect](rotatesymboleffect.md)
- [struct WiggleSymbolEffect](wigglesymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Symbols/variablecolorsymboleffect)*