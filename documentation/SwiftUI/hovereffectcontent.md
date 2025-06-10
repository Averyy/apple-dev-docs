# HoverEffectContent

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes the effects of a view for a particular hover effect phase.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol HoverEffectContent
```

#### Overview

```swift
Color.red
    .hoverEffect { effect, isActive, proxy in
        effect.opacity(isActive ? 1 : 0.5)
    }
```

You don’t conform to this protocol yourself. Instead, effects are described by calling modifier functions on other effects, like the `opacity(_:)` modifier used in the example above.

## Topics

### Instance Methods
- [func animation(Animation?, body: (EmptyHoverEffectContent) -> some HoverEffectContent) -> some HoverEffectContent](hovereffectcontent/animation(_:body:).md)
  Applies the given [`Animation`](animation.md) to all effects within the `body` closure.
- [func clipShape<S>(S, style: FillStyle) -> some HoverEffectContent](hovereffectcontent/clipshape(_:style:).md)
  Sets a clipping shape for the view.
- [func offset(CGSize) -> some HoverEffectContent](hovereffectcontent/offset(_:).md)
  Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some HoverEffectContent](hovereffectcontent/offset(x:y:).md)
  Offsets the view by the specified horizontal and vertical distances.
- [func opacity(Double) -> some HoverEffectContent](hovereffectcontent/opacity(_:).md)
  Sets the transparency of the view.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some HoverEffectContent](hovereffectcontent/rotationeffect(_:anchor:).md)
  Rotates content in two dimensions around the specified point.
- [func scaleEffect(_:anchor:)](hovereffectcontent/scaleeffect(_:anchor:).md)
  Scales the view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some HoverEffectContent](hovereffectcontent/scaleeffect(x:y:anchor:).md)
  Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func transformEffect(CGAffineTransform) -> some HoverEffectContent](hovereffectcontent/transformeffect(_:).md)
  Applies an affine transformation to the view’s rendered output.

## Relationships

### Conforming Types
- [EmptyHoverEffectContent](emptyhovereffectcontent.md)
- [ModifiedContent](modifiedcontent.md)

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
- [struct ContentHoverEffect](contenthovereffect.md)
  A `CustomHoverEffect` that applies effects to a view on hover using a closure.
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
- [struct EmptyHoverEffectContent](emptyhovereffectcontent.md)
  An empty base effect that you use to build other effects.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](view/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [struct HandPointerBehavior](handpointerbehavior.md)
  A behavior that can be applied to the hand pointer while the user is interacting with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent)*