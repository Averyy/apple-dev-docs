# glassEffectID(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Associates an identity value to Liquid Glass effects defined within this view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func glassEffectID(_ id: (some Hashable & Sendable)?, in namespace: Namespace.ID) -> some View
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Discussion

You use this modifier with the [`glassEffect(_:in:)`](view/glasseffect(_:in:).md) view modifier and a [`GlassEffectContainer`](glasseffectcontainer.md) view. When used together, SwiftUI uses the identifier to animate shapes to and from each other during transitions.

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape) -> some View](view/glasseffect(_:in:).md)
  Applies the Liquid Glass effect to a view.
- [func glassEffectTransition(GlassEffectTransition) -> some View](view/glasseffecttransition(_:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](view/glasseffectunion(id:namespace:).md)
  Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectContainer](glasseffectcontainer.md)
  A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [struct GlassEffectTransition](glasseffecttransition.md)
  A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.
- [struct GlassProminentButtonStyle](glassprominentbuttonstyle.md)
  A button style that applies prominent glass border artwork based on the button’s context.
- [struct DefaultGlassEffectShape](defaultglasseffectshape.md)
  The default shape applied by glass effects, a capsule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glasseffectid(_:in:))*