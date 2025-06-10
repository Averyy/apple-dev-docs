# hoverEffectGroup(id:in:behavior:)

**Framework**: SwiftUI  
**Kind**: method

Creates an effect that activates a named group of effects.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func hoverEffectGroup(id: String? = nil, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup) -> GroupHoverEffect
```

#### Return Value

A new effect that activates the given effect group.

#### Discussion

The effect group is uniquely identified by combining the `id` and `namespace` parameters. If an `id` is not provided, the effect will be identified by the `namespace` alone. Providing an `id` is useful when creating effects that use multiple, closely-related groups.

The default behavior of an effect is to activate the effect group when hovered. The `behavior` parameter can be used to choose alternative behaviors. See [`HoverEffectGroup.Behavior`](hovereffectgroup/behavior.md) for all possible behaviors.

## Parameters

- `id`: An optional id to give the group. If provided, the group will be   uniquely identified by combining the id and the namespace.
- `namespace`: The namespace that identifies the group. If   , this modifier has no effect.
- `behavior`: How the effect will behave relative to other   effects in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/hovereffectgroup(id:in:behavior:)-swift.type.method)*