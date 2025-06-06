# hoverEffectGroup(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hoverEffectGroup(_ group: HoverEffectGroup?) -> some View
```

#### Return Value

A view that activates the given hover group, as well as all effects added to subviews.

#### Discussion

You use this modifier when all effects defined on a view and its subviews should activate together. In the following example hovering anywhere over the view will activate the `hoverEffect`s added to the `Text` and the background view, as well as any effects added to the group by other views:

```None
struct EffectView: View {
    let effectGroup: HoverEffectGroup?

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
       .hoverEffectGroup(effectGroup)
   }
}
```

## Parameters

- `group`: The   to activate when this view or any   subviews are hovered. If  , this modifier has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent/hovereffectgroup(_:))*