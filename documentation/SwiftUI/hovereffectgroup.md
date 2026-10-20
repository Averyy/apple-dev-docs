# HoverEffectGroup

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes a grouping of effects that activate together.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct HoverEffectGroup
```

#### Overview

Use [`HoverEffectGroup`](./hovereffectgroup.md) to apply effects to multiple views in concert.

## Topics

### Structures
- [HoverEffectGroup.Behavior](./hovereffectgroup/behavior.md)
  Describes the behavior of an effect in a group.
### Initializers
- [init(Namespace.ID, behavior: HoverEffectGroup.Behavior)](./hovereffectgroup/init%28_,behavior%29.md)
  Creates a new [`HoverEffectGroup`](./hovereffectgroup.md) from a `Namespace.ID`.
- [init(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior)](./hovereffectgroup/init%28id,in,behavior%29.md)
  Creates a new [`HoverEffectGroup`](./hovereffectgroup.md).
### Instance Methods
- [func behavior(HoverEffectGroup.Behavior) -> HoverEffectGroup](./hovereffectgroup/behavior%28_%29.md)
  Returns a new version of `self` with the given `behavior`.
### Type Properties
- [static var systemOverlays: HoverEffectGroup](./hovereffectgroup/systemoverlays.md)
  A `HoverEffectGroup` that becomes active when system overlays are visible.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Changing view appearance for hover events
- [func hoverEffect(HoverEffect) -> some View](./view/hovereffect%28_%29.md)
  Applies a hover effect to this view.
- [struct HoverEffect](./hovereffect.md)
  An effect applied when the pointer hovers over a view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](./view/hovereffect%28_,in,isenabled%29.md)
  Applies a hover effect to this view, optionally adding it to a [`HoverEffectGroup`](./hovereffectgroup.md).
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](./view/hovereffect%28in,isenabled,body%29.md)
  Applies a hover effect to this view described by the given closure.
- [protocol CustomHoverEffect](./customhovereffect.md)
  A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.
- [struct ContentHoverEffect](./contenthovereffect.md)
  A `CustomHoverEffect` that applies effects to a view on hover using a closure.
- [func hoverEffectGroup() -> some View](./view/hovereffectgroup%28%29.md)
  Adds an implicit [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](./view/hovereffectgroup%28_%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](./view/hovereffectgroup%28id,in,behavior%29.md)
  Adds a [`HoverEffectGroup`](./hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [struct GroupHoverEffect](./grouphovereffect.md)
  A `CustomHoverEffect` that activates a named group of effects.
- [protocol HoverEffectContent](./hovereffectcontent.md)
  A type that describes the effects of a view for a particular hover effect phase.
- [struct EmptyHoverEffectContent](./emptyhovereffectcontent.md)
  An empty base effect that you use to build other effects.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](./view/handpointerbehavior%28_%29.md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [struct HandPointerBehavior](./handpointerbehavior.md)
  A behavior that can be applied to the hand pointer while the user is interacting with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectgroup)*