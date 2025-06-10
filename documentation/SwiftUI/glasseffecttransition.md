# GlassEffectTransition

**Framework**: SwiftUI  
**Kind**: struct

A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct GlassEffectTransition
```

## Topics

### Type Properties
- [static var identity: GlassEffectTransition](glasseffecttransition/identity.md)
  The identity transition specifying no changes.
- [static var matchedGeometry: GlassEffectTransition](glasseffecttransition/matchedgeometry.md)
  Returns the matched geometry glass effect transition.
### Type Methods
- [static func matchedGeometry(properties: MatchedGeometryProperties, anchor: UnitPoint) -> GlassEffectTransition](glasseffecttransition/matchedgeometry(properties:anchor:).md)
  Returns the matched geometry glass effect transition.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)
  Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md)
  Enhance your app experience with system-provided and custom Liquid Glass.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](view/glasseffect(_:in:isenabled:).md)
  Applies the Liquid Glass effect to a view.
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [struct GlassEffectContainer](glasseffectcontainer.md)
  A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [struct GlassButtonStyle](glassbuttonstyle.md)
  A button style that applies glass border artwork based on the button’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glasseffecttransition)*