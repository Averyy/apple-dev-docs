# hoverEffectGroup(id:in:behavior:)

**Framework**: RealityKit  
**Kind**: method

Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hoverEffectGroup(id: String? = nil, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup) -> some View
```

#### Return Value

A new effect that is matched to other effects in the same group.

#### Discussion

You use this modifier when all effects defined on a view and its subviews should activate together. In the following example hovering anywhere over the view will activate the `hoverEffect`s added to the `Text` and the background view, as well as any effects added to the group by other views:

```None
struct EffectView: View {
    @Namespace var namespace

    var body: some View {
        HStack {
            Image(systemName: "exclamationmark.triangle.fill")
            Text("12 Issues")
                .hoverEffect { effect, isActive, _ in
                    effect.opacity(isActive ? 1 : 0.5)
                }
        }
        .padding()
        .background {
            Capsule()
                .fill(.yellow)
                .hoverEffect { effect, isActive, _ in
                    effect.opacity(isActive ? 0.25 : 0.1)
                }
        }
        .hoverEffectGroup(in: namespace)
    }
}
```

The effect group is uniquely identified by combining the `id` and `namespace` parameters. If an `id` is not provided, the effect will be identified by the `namespace` alone. Providing a `name` is useful when creating effects that use multiple, related groups.

The default behavior of a matched effect is to activate the effect group when hovered. The `behavior` parameter can be used to choose alternative behaviors. See `HoverEffectGroup/Behavior` for all possible behaviors.

## Parameters

- `id`: An optional id to give the group. If provided, the group will be   uniquely identified by combining the id and the namespace.
- `namespace`: The namespace that identifies the group. If   , this modifier has no effect.
- `behavior`: How the effect will behave relative to other   effects in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/hovereffectgroup(id:in:behavior:))*