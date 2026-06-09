# glassEffectTransition(_:)

**Framework**: SwiftUI  
**Kind**: method

Associates a glass effect transition with any glass effects defined within this view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func glassEffectTransition(_ transition: GlassEffectTransition) -> some View
```

#### Discussion

You use this modifier with the [`glassEffect(_:in:)`](view/glasseffect(_:in:).md) view modifier and [`GlassEffectContainer`](glasseffectcontainer.md) view. When used together, SwiftUI will use the provided transition to apply changes to the glass effect when you add or remove views with these effects from the view hierarchy.

In the example below, the notepad image will transition into and out of the pencil image when the isExpanded variable changes.

```swift
var isExpanded: Bool
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 10.0) {
        HStack(spacing: 10.0) {
            Image(systemName: "pencil")
                .frame(width: 20.0, height: 20.0)
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

                if isExpanded {
                    Image(systemName: "note")
                        .frame(width: 20.0, height: 20.0)
                        .glassEffect()
                        .glassEffectID("note", in: namespace)
                        .glassEffectTransition(.matchedGeometry)
                }
            }
        }
    }
}
```

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape) -> some View](view/glasseffect(_:in:).md)
  Applies the Liquid Glass effect to a view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](view/glasseffectid(_:in:).md)
  Associates an identity value to Liquid Glass effects defined within this view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glasseffecttransition(_:))*