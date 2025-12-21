# ContentHoverEffect

**Framework**: SwiftUI  
**Kind**: struct

A `CustomHoverEffect` that applies effects to a view on hover using a closure.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct ContentHoverEffect<Effect> where Effect : HoverEffectContent
```

#### Overview

Use the [`hoverEffect(in:isEnabled:body:)`](customhovereffect/hovereffect(in:isenabled:body:)-swift.type.method.md) method or the `CustomHoverEffect/hoverEffect(in:isEnabled:body:)` or [`hoverEffect(in:isEnabled:body:)`](view/hovereffect(in:isenabled:body:).md) modifiers to create content effects.

## Relationships

### Conforms To
- [CustomHoverEffect](customhovereffect.md)

## See Also

- [func hoverEffect(HoverEffect) -> some View](view/hovereffect(_:).md)
  Applies a hover effect to this view.
- [struct HoverEffect](hovereffect.md)
  An effect applied when the pointer hovers over a view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](view/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a [`HoverEffectGroup`](hovereffectgroup.md).
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](view/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [protocol CustomHoverEffect](customhovereffect.md)
  A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [struct HoverEffectGroup](hovereffectgroup.md)
  Describes a grouping of effects that activate together.
- [func hoverEffectGroup() -> some View](view/hovereffectgroup.md)
  Adds an implicit [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](view/hovereffectgroup(_:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](view/hovereffectgroup(id:in:behavior:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [struct GroupHoverEffect](grouphovereffect.md)
  A `CustomHoverEffect` that activates a named group of effects.
- [protocol HoverEffectContent](hovereffectcontent.md)
  A type that describes the effects of a view for a particular hover effect phase.
- [struct EmptyHoverEffectContent](emptyhovereffectcontent.md)
  An empty base effect that you use to build other effects.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](view/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [struct HandPointerBehavior](handpointerbehavior.md)
  A behavior that can be applied to the hand pointer while the user is interacting with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenthovereffect)*