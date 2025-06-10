# hoverEffectGroup(id:in:behavior:)

**Framework**: SwiftUI  
**Kind**: method

Activates this effect as part of an effect group.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func hoverEffectGroup(id: String? = nil, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup) -> some CustomHoverEffect
```

#### Return Value

A new effect that activates with other effects in the same group.

#### Discussion

You use this method to compose effects that change multiple views in concert. In the following example, both views’ effects are in the same group. As a result, hovering over either view will activate all effects in the group, causing both views to become fully opaque:

```swift
struct EffectView: View {
    @Namespace var namespace

    var body: some View {
        Color.red
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(in: namespace)
            )
        Color.blue
            .frame(width: 100, height: 100)
            .hoverEffect(
                FadeEffect().hoverEffectGroup(in: namespace)
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

The effect group is uniquely identified by combining the `id` and `namespace` parameters. If an `id` is not provided, the effect will be identified by the `namespace` alone. Providing an `id` is useful when creating effects that use multiple, closely-related groups.

The default behavior of an effect is to activate the effect group when hovered. The `behavior` parameter can be used to choose alternative behaviors. See [`HoverEffectGroup.Behavior`](hovereffectgroup/behavior.md) for all possible behaviors.

## Parameters

- `id`: An optional id to give the group. If provided, the group will be   uniquely identified by combining the id and the namespace.
- `namespace`: The namespace that identifies the group. If   , this modifier has no effect.
- `behavior`: How the effect will behave relative to other   effects in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.method)*