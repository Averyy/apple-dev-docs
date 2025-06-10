# defaultHoverEffect(_:)

**Framework**: SwiftUI  
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

Use this modifier to set a specific hover effect for all views with the [`hoverEffect(_:)`](view/hovereffect(_:).md) modifier applied within a view. The default effect is typically used when no [`HoverEffect`](hovereffect.md) was provided or if [`automatic`](hovereffect/automatic.md) is specified.

For example, this view uses [`highlight`](hovereffect/highlight.md) for both the red and green Color views:

```swift
HStack {
    Color.red.hoverEffect()
    Color.green.hoverEffect()
}
.defaultHoverEffect(.highlight)
```

This also works for customizing the default hover effect in views like [`Button`](button.md)s when using a SwiftUI-defined style like `ButtonStyle/bordered`, which can provide a hover effect by default. For example, this view replaces the hover effect for a [`Button`](button.md) with [`highlight`](hovereffect/highlight.md):

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

## See Also

- [func onHover(perform: (Bool) -> Void) -> some View](view/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onContinuousHover(coordinateSpace:perform:)](view/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func hoverEffect(_:isEnabled:)](view/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffectDisabled(Bool) -> some View](view/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [var isHoverEffectEnabled: Bool](environmentvalues/ishovereffectenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [enum HoverPhase](hoverphase.md)
  The current hovering state and value of the pointer.
- [struct HoverEffectPhaseOverride](hovereffectphaseoverride.md)
  Options for overriding a hover effect’s current phase.
- [struct OrnamentHoverContentEffect](ornamenthovercontenteffect.md)
  Presents an ornament on hover using a custom effect.
- [struct OrnamentHoverEffect](ornamenthovereffect.md)
  Presents an ornament on hover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaulthovereffect(_:))*