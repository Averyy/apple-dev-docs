# defaultHoverEffect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
nonisolated
func defaultHoverEffect(_ effect: HoverEffect?) -> some View
```

## Return Value

A view that uses `effect` as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the [`hoverEffect(_:)`](./hovereffect%28_%29.md) modifier applied to them within a view hierarchy. The default effect is typically used when no [`CustomHoverEffect`](../customhovereffect.md) was provided or if [`automatic`](../customhovereffect/automatic.md) is specified.

For example, this view applies a custom effect named `FadeInHoverEffect` for both the red and green Color views:

```swift
HStack {
    Color.red.hoverEffect()
    Color.green.hoverEffect()
}
.defaultHoverEffect(FadeInHoverEffect())
```

This also works for customizing the default hover effect in views like [`Button`](../button.md)s when using a SwiftUI-defined style like `ButtonStyle/bordered`, which can provide a hover effect by default. For example, this view replaces the hover effect for a [`Button`](../button.md) with a `FadeInHoverEffect` effect:

```swift
Button("Next") {
    // perform action
}
.buttonStyle(.bordered)
.defaultHoverEffect(FadeInHoverEffect())
```

## Parameters

- `effect`: The default hover effect to use within this view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaulthovereffect(_:)-4vsau)*