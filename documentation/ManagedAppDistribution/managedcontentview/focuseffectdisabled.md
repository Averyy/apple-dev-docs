# focusEffectDisabled(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func focusEffectDisabled(_ disabled: Bool = true) -> some View
```

#### Return Value

A view that controls whether focus effects can be displayed in this view.

#### Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button does not display a focus effect because the outer `focusEffectDisabled(_:)` modifier overrides the inner one:

```None
HStack {
    Button("Press") {}
        .focusEffectDisabled(false)
}
.focusEffectDisabled(true)
```

## Parameters

- `disabled`: A Boolean value that determines whether this view   can display focus effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/focuseffectdisabled(_:))*