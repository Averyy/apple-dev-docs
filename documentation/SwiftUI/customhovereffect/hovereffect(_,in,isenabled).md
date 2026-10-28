# hoverEffect(_:in:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies this effect in parallel with the given `effect`.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func hoverEffect(_ effect: some CustomHoverEffect, in group: HoverEffectGroup? = nil, isEnabled: Bool = true) -> some CustomHoverEffect
```

## Discussion

Use `hoverEffect(_:)` to combine two effects into a single effect that applies both effects in parallel. Modifiers like [`hoverEffectDisabled(_:)`](./hovereffectdisabled%28_%29.md) applied to `effect` will not apply to this effect.

For example, in the following effect only the `ScaleUpEffect` is disabled, since modifiers applied to that effect are applied independently.

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

- `effect`: A [`CustomHoverEffect`](../customhovereffect.md) to combine with this effect.
- `group`: An optional [`HoverEffectGroup`](../hovereffectgroup.md) to add this effect to.
- `isEnabled`: Whether `effect` is enabled or not.

## See Also

### Creating custom hover effects
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect](./hovereffect%28in,isenabled,body%29-swift.method.md)
  Applies a hover effect based on the current phase.
- [func hoverEffectGroup(HoverEffectGroup?) -> some CustomHoverEffect](./hovereffectgroup%28_%29-swift.method.md)
  Activates this effect as part of an effect group.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some CustomHoverEffect](./hovereffectgroup%28id,in,behavior%29-swift.method.md)
  Activates this effect as part of an effect group.
- [func hoverEffectDisabled(Bool) -> some CustomHoverEffect](./hovereffectdisabled%28_%29.md)
  Disables this hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffect(_:in:isenabled:))*