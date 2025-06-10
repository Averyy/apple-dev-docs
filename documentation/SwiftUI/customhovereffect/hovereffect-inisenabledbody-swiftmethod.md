# hoverEffect(in:isEnabled:body:)

**Framework**: SwiftUI  
**Kind**: method

Applies a hover effect based on the current phase.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func hoverEffect(in group: HoverEffectGroup? = nil, isEnabled: Bool = true, body: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect
```

#### Return Value

A new effect that changes a view’s appearance when hovered.

#### Discussion

You use this modifier to describe how a view should change when hovered. The given closure is provided an empty effect that you use to compose an effect, as well as a boolean describing which phase is being requested. A [`GeometryProxy`](geometryproxy.md) is also provided, allowing effects to change based on the view’s geometry.

In the following example, the effect will apply a scale of 1.0 to a view when inactive, and then scale to 1.1 when active:

```swift
struct ScaleHoverEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, proxy in
            effect.scaleEffect(!isActive ? 1.0 : 1.1)
        }
    }
}
```

Use the [`animation(_:body:)`](hovereffectcontent/animation(_:body:).md) modifier to specify how visual changes should be animated.

## Parameters

- `group`: An optional   to add this effect to.
- `isEnabled`: Whether the effect is enabled or not. If  , the   effect’s inactive state will be applied, and it will not apply the   active state when hovered.
- `body`: The closure that constructs a   for   each of the effect’s phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(in:isenabled:body:)-swift.method)*