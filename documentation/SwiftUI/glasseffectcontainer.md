# GlassEffectContainer

**Framework**: SwiftUI  
**Kind**: struct

A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.

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
@preconcurrency struct GlassEffectContainer<Content> where Content : View
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Overview

Use a container with the [`glassEffect(_:in:)`](view/glasseffect(_:in:).md) modifier. Each view with a Liquid Glass effect contributes a shape rendered with the effect to a set of shapes. SwiftUI renders the effects together, improving rendering performance and allowing the effects to interact with and morph into one another.

Configure how shapes interact with one another by customizing the default spacing value of the container. As shapes near one another, their paths start to blend into one another. The higher the spacing, the sooner blending begins as the shapes approach each other.

## Topics

### Initializers
- [init(spacing: CGFloat?, content: () -> Content)](glasseffectcontainer/init(spacing:content:).md)
  Creates a glass effect container with the provided spacing, extracting glass shapes from the provided content.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](view.md)

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape) -> some View](view/glasseffect(_:in:).md)
  Applies the Liquid Glass effect to a view.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectTransition](glasseffecttransition.md)
  A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.
- [struct GlassProminentButtonStyle](glassprominentbuttonstyle.md)
  A button style that applies prominent glass border artwork based on the button’s context.
- [struct DefaultGlassEffectShape](defaultglasseffectshape.md)
  The default shape applied by glass effects, a capsule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glasseffectcontainer)*