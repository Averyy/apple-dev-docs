# OrnamentHoverEffect

**Framework**: SwiftUI  
**Kind**: struct

Presents an ornament on hover.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct OrnamentHoverEffect<OrnamentView> where OrnamentView : View
```

#### Overview

You don’t use this directly. Use `CustomHoverEffect.ornament` to create ornament effects instead.

## Relationships

### Conforms To
- [CustomHoverEffect](customhovereffect.md)

## See Also

- [func onHover(perform: (Bool) -> Void) -> some View](view/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/ornamenthovereffect)*