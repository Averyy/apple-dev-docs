# hoverEffect(_:in:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Applies this effect in parallel with the given `effect`.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func hoverEffect(_ effect: some CustomHoverEffect, in group: HoverEffectGroup? = nil, isEnabled: Bool = true) -> some CustomHoverEffect
```

#### Discussion

Use `hoverEffect(_:)` to combine two effects into a single effect that applies both effects in parallel. Modifiers like [`hoverEffectDisabled(_:)`](customhovereffect/hovereffectdisabled(_:).md) applied to `effect` will not apply to this effect.

For example, in the following effect only the `ScaleUpEffect` will be disabled, since modifiers applied to that effect will applied independently.

```swift
struct FadeAndScaleEffect: CustomHoverEffect {
    @Environment(\.accessibilityReduceMotion) var accessibilityReduceMotion
    func body(content: Content) -> some CustomHoverEffect {
        content
            .hoverEffect { effect, isActive, _ in
                effect.opacity(isActive ? 1 : 0.9)
            }
            .hoverEffect(
                ScaleUpEffect().hoverEffectDisabled(accessibilityReduceMotion)
            )
    }
}

struct ScaleUpEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, _ in
            effect.scaleEffect(isActive ? 1.05 : 1.0)
        }
    }
}
```

- Returns a new effect that applies both effects in parallel.

## Parameters

- `effect`: A   to combine with this effect.
- `group`: An optional   to add this effect to.
- `isEnabled`: Whether   is enabled or not.

## See Also

- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect](customhovereffect/hovereffect(in:isenabled:body:).md)
  Applies a hover effect based on the current phase.
- [func hoverEffectGroup(HoverEffectGroup?) -> some CustomHoverEffect](customhovereffect/hovereffectgroup(_:).md)
  Activates this effect as part of an effect group.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some CustomHoverEffect](customhovereffect/hovereffectgroup(id:in:behavior:).md)
  Activates this effect as part of an effect group.
- [func hoverEffectDisabled(Bool) -> some CustomHoverEffect](customhovereffect/hovereffectdisabled(_:).md)
  Disables this hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(_:in:isenabled:))*