# defaultHoverEffect(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the default hover effect to use within this view hierarchy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func defaultHoverEffect(_ effect: some CustomHoverEffect) -> some View
```

#### Return Value

A view that uses `effect` as the default hover effect.

#### Discussion

Use this modifier to set a specific hover effect for all views with the `View/hoverEffect(_:)` modifier applied to them within a view hierarchy. The default effect is typically used when no `CustomHoverEffect` was provided or if `CustomHoverEffect/automatic` is specified.

For example, this view applies a custom effect named `FadeInHoverEffect` for both the red and green Color views:

```swift
HStack {
    Color.red.hoverEffect()
    Color.green.hoverEffect()
}
.defaultHoverEffect(FadeInHoverEffect())
```

This also works for customizing the default hover effect in views like `Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`, which can provide a hover effect by default. For example, this view replaces the hover effect for a `Button` with a `FadeInHoverEffect` effect:

```swift
Button("Next") {
    // perform action
}
.buttonStyle(.bordered)
.defaultHoverEffect(FadeInHoverEffect())
```

## Parameters

- `effect`: The default hover effect to use within this view   hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/defaulthovereffect(_:)-5vomu)*