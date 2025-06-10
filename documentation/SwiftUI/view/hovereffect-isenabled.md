# hoverEffect(_:isEnabled:)

**Framework**: SwiftUI  
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

By default, [`automatic`](hovereffect/automatic.md) is used. You can control the behavior of the automatic effect with the [`defaultHoverEffect(_:)`](view/defaulthovereffect(_:).md) modifier.

## Parameters

- `effect`: The effect to apply to this view.
- `isEnabled`: Whether the effect is enabled or not.

## See Also

- [func onHover(perform: (Bool) -> Void) -> some View](view/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onContinuousHover(coordinateSpace:perform:)](view/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func hoverEffectDisabled(Bool) -> some View](view/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func defaultHoverEffect(_:)](view/defaulthovereffect(_:).md)
  Sets the default hover effect to use for views within this view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/hovereffect(_:isenabled:))*