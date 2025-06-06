# init(id:in:behavior:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new [`HoverEffectGroup`](hovereffectgroup.md).

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(id: String?, in namespace: Namespace.ID, behavior: HoverEffectGroup.Behavior = .activatesGroup)
```

#### Return Value

A new HoverEffectGroup

## Parameters

- `id`: An optional id to give the group. If provided, the group will be   uniquely identified by combining the id and the namespace.
- `namespace`: The namespace that identifies the group.
- `behavior`: How the effect will behave relative to other   effects in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectgroup/init(id:in:behavior:))*