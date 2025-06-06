# hoverEffect(_:isEnabled:)

**Framework**: DeviceActivity  
**Kind**: method

Applies a hover effect to this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func hoverEffect(_ effect: HoverEffect = .automatic, isEnabled: Bool = true) -> some View
```

#### Return Value

A new view that applies a hover effect to `self`.

#### Discussion

By default, `HoverEffect/automatic` is used. You can control the behavior of the automatic effect with the `View/defaultHoverEffect(_:)` modifier.

## Parameters

- `effect`: The effect to apply to this view.
- `isEnabled`: Whether the effect is enabled or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/hovereffect(_:isenabled:)-2mwj3)*