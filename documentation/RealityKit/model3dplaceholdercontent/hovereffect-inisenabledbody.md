# hoverEffect(in:isEnabled:body:)

**Framework**: RealityKit  
**Kind**: method

Applies a hover effect to this view described by the given closure.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hoverEffect(in group: HoverEffectGroup? = nil, isEnabled: Bool = true, body: @escaping (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View
```

#### Return Value

A new effect that changes a view’s appearance when hovered.

#### Discussion

You use this modifier to describe how a view should change when hovered. The given block is provided an empty effect that you use to compose effects, as well as a boolean describing which phase is being requested. A `GeometryProxy` is also provided, allowing effects to change based on the view’s geometry.

In the following example, the `Text` will have a scale of 1.0 when inactive, and then scale to 1.1 when hovered:

```None
Text("Hello, World!")
    .hoverEffect { effect, isActive, proxy in
        effect.scaleEffect(!isActive ? 1.0 : 1.1)
    }
```

Use the `HoverEffectContent/animation(_:body:)` modifier to specify how visual changes should be animated.

## Parameters

- `group`: An optional   to add this effect to.
- `isEnabled`: Whether the effect is enabled or not. If  , the   effect’s inactive state will be applied, and it will not apply the   active state when hovered.
- `body`: The closure that constructs a   for   each of the effect’s phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent/hovereffect(in:isenabled:body:))*