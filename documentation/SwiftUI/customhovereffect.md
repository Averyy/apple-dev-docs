# CustomHoverEffect

**Framework**: SwiftUI  
**Kind**: protocol

A type that represents how a view should change when a pointer hovers over a view, or when someone looks at the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol CustomHoverEffect
```

#### Overview

Custom hover effects apply their inactive values when the effect is inactive, and their active values when the effect is active. For example, the following effect causes a view to be partially transparent when inactive, but animate to fully opaque when active:

```swift
struct FadeInHoverEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, proxy in
            effect.animation(.easeOut) {
                $0.opacity(isActive ? 1 : 0.5)
            }
        }
    }
}
```

This effect can be applied to a view using the `hoverEffect(_:)` modifier:

```swift
Color.red
    .hoverEffect(FadeInHoverEffect())
```

Hover effects do not affect a view’s layout, and may be applied to a view out-of-process. Therefore an effect’s current phase may not be visible within your app.

## Topics

### Getting built-in hover effects
- [static var automatic: AutomaticHoverEffect](customhovereffect/automatic.md)
  The default hover effect based on the surrounding context.
- [static var empty: EmptyHoverEffect](customhovereffect/empty.md)
  An effect that applies no changes when hovered.
- [static var highlight: HighlightHoverEffect](customhovereffect/highlight.md)
  A hover effect that highlights views using a light source to indicate position.
- [static var lift: LiftHoverEffect](customhovereffect/lift.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
### Creating custom hover effects
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some CustomHoverEffect](customhovereffect/hovereffect(_:in:isenabled:).md)
  Applies this effect in parallel with the given `effect`.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect](customhovereffect/hovereffect(in:isenabled:body:).md)
  Applies a hover effect based on the current phase.
- [func hoverEffectGroup(HoverEffectGroup?) -> some CustomHoverEffect](customhovereffect/hovereffectgroup(_:).md)
  Activates this effect as part of an effect group.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some CustomHoverEffect](customhovereffect/hovereffectgroup(id:in:behavior:).md)
  Activates this effect as part of an effect group.
- [func hoverEffectDisabled(Bool) -> some CustomHoverEffect](customhovereffect/hovereffectdisabled(_:).md)
  Disables this hover effect.
### Supporting types
- [struct AutomaticHoverEffect](automatichovereffect.md)
  The default hover effect based on the surrounding context.
- [struct EmptyHoverEffect](emptyhovereffect.md)
  A base hover effect used to build additional effects.
- [struct HighlightHoverEffect](highlighthovereffect.md)
  A hover effect that highlights views using a light source to indicate position.
- [struct LiftHoverEffect](lifthovereffect.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.
### Associated Types
- [associatedtype Body : CustomHoverEffect](customhovereffect/body.md)
  The type of effect representing the body of this effect. When you create a custom effect, Swift infers this type from your implementation of the required [`body(content:)`](customhovereffect/body(content:).md) method.
### Instance Methods
- [func body(content: Self.Content) -> Self.Body](customhovereffect/body(content:).md)
  Defines the effect produced by this effect.
### Type Aliases
- [CustomHoverEffect.Content](customhovereffect/content.md)
  The content effect type passed to `body(content:)`.

## Relationships

### Conforming Types
- [AutomaticHoverEffect](automatichovereffect.md)
- [EmptyHoverEffect](emptyhovereffect.md)
- [HighlightHoverEffect](highlighthovereffect.md)
- [HoverEffect](hovereffect.md)
- [LiftHoverEffect](lifthovereffect.md)
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
- [struct HoverEffectGroup](hovereffectgroup.md)
  Describes a grouping of effects that activate together.
- [func hoverEffectGroup() -> some View](view/hovereffectgroup.md)
  Adds an implicit [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](view/hovereffectgroup(_:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](view/hovereffectgroup(id:in:behavior:).md)
  Adds a [`HoverEffectGroup`](hovereffectgroup.md) to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [protocol HoverEffectContent](hovereffectcontent.md)
  A type that describes the effects of a view for a particular hover effect phase.
- [struct EmptyHoverEffectContent](emptyhovereffectcontent.md)
  An empty base effect that you use to build other effects.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](view/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [struct HandPointerBehavior](handpointerbehavior.md)
  A behavior that can be applied to the hand pointer while the user is interacting with a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect)*