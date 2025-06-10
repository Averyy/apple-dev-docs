# glassEffect(_:in:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Applies the Liquid Glass effect to a view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func glassEffect(_ glass: Glass = .regular, in shape: some Shape = .capsule, isEnabled: Bool = true) -> some View
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Discussion

When you use this effect, the system:

- Renders a shape anchored behind a view with the Liquid Glass material.
- Applies the foreground effects of Liquid Glass over a view.

For example, to add this effect to a [`Text`](text.md):

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

SwiftUI uses the [`regular`](glass/regular.md) variant by default along with a [`Capsule`](capsule.md) shape.

SwiftUI anchors the Liquid Glass to a view’s bounds. For the example above, the material fills the entirety of the `Text` frame, which includes the padding.

You typically use this modifier with a [`GlassEffectContainer`](glasseffectcontainer.md) to combine multiple Liquid Glass shapes into a single shape that can morph into one another.

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectContainer](glasseffectcontainer.md)
  A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [struct GlassEffectTransition](glasseffecttransition.md)
  A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:isenabled:))*