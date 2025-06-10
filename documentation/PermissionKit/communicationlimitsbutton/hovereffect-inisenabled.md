# hoverEffect(_:in:isEnabled:)

**Framework**: PermissionKit  
**Kind**: method

Applies a hover effect to this view, optionally adding it to a `HoverEffectGroup`.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hoverEffect(_ effect: some CustomHoverEffect, in group: HoverEffectGroup?, isEnabled: Bool = true) -> some View
```

#### Return Value

A new view that applies the hover effect to `self` whenever the view is hovered, or the `HoverEffectGroup` is activated.

## Parameters

- `effect`: The effect to apply to this view.
- `group`: An optional   the effect should belong to.
- `isEnabled`: Whether this effect is enabled or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/hovereffect(_:in:isenabled:))*