# hoverEffect(in:isEnabled:body:)

**Framework**: SwiftUI  
**Kind**: method

Creates a hover effect that applies effects to a view using the given closure.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func hoverEffect<C>(in group: HoverEffectGroup? = nil, isEnabled: Bool = true, body: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> C) -> ContentHoverEffect<C> where Self == ContentHoverEffect<C>, C : HoverEffectContent
```

#### Return Value

A new effect that applies effects to a view using the given body closure.

#### Discussion

The closure is provided an empty effect that you use to compose effects, as well as a boolean describing which phase is being requested. A [`GeometryProxy`](geometryproxy.md) is also provided, allowing effects to change based on the view’s geometry.

Typically the `CustomHoverEffect/hoverEffect(in:isEnabled:body:)` or [`hoverEffect(in:isEnabled:body:)`](view/hovereffect(in:isenabled:body:).md) modifiers are used to create effects. Use this method when you need to create effects in other contexts.

For example, the following code uses this method and [`HoverEffect`](hovereffect.md) to create a type-erased fade effect:

```swift
HoverEffect(
    .hoverEffect { e, isActive, _ in
        e.opacity(isActive ? 1 : 0)
    }
)
```

## Parameters

- `group`: An optional   to add this effect to.
- `isEnabled`: Whether the effect is enabled or not. If  , the   effect will not become active when hovered.
- `body`: The closure that constructs a   for   each of the effect’s phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.type.method)*