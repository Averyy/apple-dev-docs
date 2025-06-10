# GlassButtonStyle

**Framework**: SwiftUI  
**Kind**: struct

A button style that applies glass border artwork based on the button’s context.

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
struct GlassButtonStyle
```

#### Overview

You can also use [`glass`](primitivebuttonstyle/glass.md) to construct this style.

## Topics

### Initializers
- [init()](glassbuttonstyle/init.md)
  Creates a glass button style.
### Instance Methods
- [func makeBody(configuration: GlassButtonStyle.Configuration) -> some View](glassbuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.

## Relationships

### Conforms To
- [PrimitiveButtonStyle](primitivebuttonstyle.md)

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
- [struct GlassEffectTransition](glasseffecttransition.md)
  A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbuttonstyle)*