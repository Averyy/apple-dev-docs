# matchedGeometry

**Framework**: SwiftUI  
**Kind**: property

Returns the matched geometry glass effect transition.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var matchedGeometry: GlassEffectTransition { get }
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Discussion

The matched geometry transition allows the geometries of glass shapes during an appearance or disappearance phase of a transition to be derived from the geometry of a nearby shape within the glass container.

For example, if a newly appearing shape is within the spacing of any existing shape, it will use that shapes geometry to transition out of.

When using the [`default`](animation/default.md), this transition applies additional scale and offset effects to content when the identity of the shape does not change but its content does. Opt out of these additional animations by providing a specific animation like [`spring`](animation/spring.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glasseffecttransition/matchedgeometry)*