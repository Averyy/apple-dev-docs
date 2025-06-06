# defaultHoverEffect(_:)

**Framework**: MusicKit  
**Kind**: method

Sets the default hover effect to use for views within this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func defaultHoverEffect(_ effect: HoverEffect?) -> some View
```

#### Return Value

A view that uses this effect as the default hover effect.

#### Discussion

Use this modifier to set a specific hover effect for all views with the `View/hoverEffect(_:)` modifier applied within a view. The default effect is typically used when no `HoverEffect` was provided or if `HoverEffect/automatic` is specified.

For example, this view uses `HoverEffect/highlight` for both the red and green Color views:

```swift
HStack {
    Color.red.hoverEffect()
    Color.green.hoverEffect()
}
.defaultHoverEffect(.highlight)
```

This also works for customizing the default hover effect in views like `Button`s when using a SwiftUI-defined style like `ButtonStyle/bordered`, which can provide a hover effect by default. For example, this view replaces the hover effect for a `Button` with `HoverEffect/highlight`:

```swift
Button("Next") {}
    // perform action
}
.buttonStyle(.bordered)
.defaultHoverEffect(.highlight)
```

Use a `nil` effect to indicate that the default hover effect should not be modified.

## Parameters

- `effect`: The default hover effect to use for views within   this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/defaulthovereffect(_:)-1zf7h)*