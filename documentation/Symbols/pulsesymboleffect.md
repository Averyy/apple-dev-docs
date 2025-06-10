# PulseSymbolEffect

**Framework**: Symbols  
**Kind**: struct

A type that fades the opacity of some or all layers in a symbol-based image.

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
struct PulseSymbolEffect
```

#### Overview

A pulse animation applies an opacity ramp to the layers in a symbol. You can choose to animate only layers marked as “always-pulses” or all layers simultaneously. Participating layers reduce their opacity to a minimum value before returning to fully opaque.

> ❗ **Important**:  Because SwiftUI is a state-driven framework, you pass a `value` parameter when adding discrete effects, like bounce. You trigger the animation by changing the `value` parameter. Because AppKit and UIKit are event-driven frameworks, discrete effects animate automatically when added to an image view.

```swift
// Add an effect in SwiftUI.
@State private var value1 = 0
@State private var value2 = 0
var body: some View {
    HStack {
        Image(systemName: "person.text.rectangle")
            // Pulse only layers marked as "always-pulse."
            .symbolEffect(.pulse, value: value1)
            .onTapGesture {
                value1 += 1
            }
        Image(systemName: "person.text.rectangle")
            // Pulse all layers three times simultaneously.
            .symbolEffect(.pulse.wholeSymbol, options: .repeat(3), value: value2)
            .onTapGesture {
                value2 += 1
            }
    }
}
```

```swift
// Add an effect in AppKit and UIKit.
// Pulse only layers marked as "always-pulse."
imageView1.addSymbolEffect(.pulse.byLayer, options: .nonRepeating)
    
// Pulse all layers three times simultaneously.
imageView2.addSymbolEffect(.pulse.wholeSymbol, options: .repeat(3))
```

## Topics

### Determining effect scope
- [var byLayer: PulseSymbolEffect](pulsesymboleffect/bylayer.md)
  An effect requesting an animation that pulses only the layers marked to always pulse.
- [var wholeSymbol: PulseSymbolEffect](pulsesymboleffect/wholesymbol.md)
  An effect requesting an animation that pulses all layers simultaneously.
### Accessing the configuration
- [var configuration: SymbolEffectConfiguration](pulsesymboleffect/configuration.md)
  The configuration for the effect.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiscreteSymbolEffect](discretesymboleffect.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IndefiniteSymbolEffect](indefinitesymboleffect.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [struct ReplaceSymbolEffect](replacesymboleffect.md)
  A type that replaces the layers of one symbol-based image with those of another.
- [struct ScaleSymbolEffect](scalesymboleffect.md)
  A type that scales the layers in a symbol-based image separately or as a whole.
- [struct VariableColorSymbolEffect](variablecolorsymboleffect.md)
  A type that replaces the opacity of variable layers in a symbol-based image in a repeatable sequence.
- [struct BreatheSymbolEffect](breathesymboleffect.md)
- [struct RotateSymbolEffect](rotatesymboleffect.md)
- [struct WiggleSymbolEffect](wigglesymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/pulsesymboleffect)*