# GlassEffectTransition

**Framework**: SwiftUI  
**Kind**: struct

A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct GlassEffectTransition
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

## Topics

### Type Properties
- [static var identity: GlassEffectTransition](glasseffecttransition/identity.md)
  The identity transition specifying no changes.
- [static var matchedGeometry: GlassEffectTransition](glasseffecttransition/matchedgeometry.md)
  Returns the matched geometry glass effect transition.
- [static var materialize: GlassEffectTransition](glasseffecttransition/materialize.md)
  The materialize glass effect transition which will fade in content and animate in or out the glass material but will not attempt to match the geometry of any other glass effects.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape) -> some View](view/glasseffect(_:in:).md)
  Applies the Liquid Glass effect to a view.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectContainer](glasseffectcontainer.md)
  A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.
- [struct GlassProminentButtonStyle](glassprominentbuttonstyle.md)
  A button style that applies prominent glass border artwork based on the button’s context.
- [struct DefaultGlassEffectShape](defaultglasseffectshape.md)
  The default shape applied by glass effects, a capsule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glasseffecttransition)*