# GeometryEffect

**Framework**: SwiftUI  
**Kind**: protocol

An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol GeometryEffect : Animatable, ViewModifier, _RemoveGlobalActorIsolation where Self.Body == Never
```

#### Overview

The only change the effect makes to the view’s ancestors and descendants is to change the coordinate transform to and from them.

## Topics

### Applying effects
- [func effectValue(size: CGSize) -> ProjectionTransform](geometryeffect/effectvalue(size:).md)
  Returns the current value of the effect.
- [func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>](geometryeffect/ignoredbylayout.md)
  Returns an effect that produces the same geometry transform as this effect, but only applies the transform while rendering its view.

## Relationships

### Inherits From
- [Animatable](animatable.md)
- [ViewModifier](viewmodifier.md)

## See Also

- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](view/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [struct MatchedGeometryProperties](matchedgeometryproperties.md)
  A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [struct Namespace](namespace.md)
  A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [func geometryGroup() -> some View](view/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryeffect)*