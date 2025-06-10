# onHover(perform:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the user moves the pointer over or away from the view’s frame.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onHover(perform action: @escaping (Bool) -> Void) -> some View
```

#### Return Value

A view that triggers `action` when the pointer enters or exits this view’s frame.

#### Discussion

Calling this method defines a region for detecting pointer movement with the size and position of this view.

## Parameters

- `action`: The action to perform whenever the pointer enters or   exits this view’s frame. If the pointer is in the view’s frame, the    closure passes   as a parameter; otherwise,  .

## See Also

- [func onContinuousHover(coordinateSpace:perform:)](view/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func hoverEffect(_:isEnabled:)](view/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onhover(perform:))*