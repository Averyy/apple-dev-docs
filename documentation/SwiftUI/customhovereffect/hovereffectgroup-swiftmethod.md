# hoverEffectGroup(_:)

**Framework**: SwiftUI  
**Kind**: method

Activates this effect as part of an effect group.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func hoverEffectGroup(_ group: HoverEffectGroup?) -> some CustomHoverEffect
```

#### Return Value

A new effect that activates with other effects in the same group.

#### Discussion

You use this method to compose effects that affect multiple views in concert. In the following example, both views’ effects are in the same group. As a result, hovering over either view will activate all effects in the group, causing both views to become fully opaque:

```swift
struct EffectView: View {
    var effectGroup: HoverEffectGroup?

    var body: some View {
        Color.red
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(effectGroup)
            )
        Color.blue
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(effectGroup)
            )
    }
}

struct FadeEffect: CustomHoverEffect {
    func body(content: Content) -> some CustomHoverEffect {
        content.hoverEffect { effect, isActive, _ in
            effect.opacity(isActive ? 1 : 0.5)
        }
    }
}
```

## Parameters

- `group`: The   to activate when this view is hovered.   If  , this modifier has no effect.

## See Also

- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some CustomHoverEffect](customhovereffect/hovereffect(_:in:isenabled:).md)
  Applies this effect in parallel with the given `effect`.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some CustomHoverEffect](customhovereffect/hovereffect(in:isenabled:body:)-swift.method.md)
  Applies a hover effect based on the current phase.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some CustomHoverEffect](customhovereffect/hovereffectgroup(id:in:behavior:)-swift.method.md)
  Activates this effect as part of an effect group.
- [func hoverEffectDisabled(Bool) -> some CustomHoverEffect](customhovereffect/hovereffectdisabled(_:).md)
  Disables this hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(_:)-swift.method)*