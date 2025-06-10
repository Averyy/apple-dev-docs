# hoverEffectDisabled(_:)

**Framework**: PermissionKit  
**Kind**: method

Adds a condition that controls whether this view can display hover effects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func hoverEffectDisabled(_ disabled: Bool = true) -> some View
```

#### Return Value

A view that controls whether hover effects can be displayed in this view.

#### Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button does not display a hover effect because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

```None
HStack {
    Button("Press") {}
        .hoverEffectDisabled(false)
}
.hoverEffectDisabled(true)
```

## Parameters

- `disabled`: A Boolean value that determines whether this view   can display hover effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/hovereffectdisabled(_:))*