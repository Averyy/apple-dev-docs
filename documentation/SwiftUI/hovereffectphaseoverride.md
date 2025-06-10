# HoverEffectPhaseOverride

**Framework**: SwiftUI  
**Kind**: struct

Options for overriding a hover effect’s current phase.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct HoverEffectPhaseOverride
```

#### Overview

By default hover effects transition between the active and inactive phases in response to hover events. Use `HoverEffectPhaseOverride` to cause a hover effect to transition between phases based on other criteria.

## Topics

### Type Properties
- [static var active: HoverEffectPhaseOverride](hovereffectphaseoverride/active.md)
  Immediately transition to the active phase.
- [static var inactive: HoverEffectPhaseOverride](hovereffectphaseoverride/inactive.md)
  Immediately transition to the inactive phase.
### Type Methods
- [static func activeTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride](hovereffectphaseoverride/activetemporarily(trigger:).md)
  Temporaily transitions to the active phase until all animations finish, and the transition is complete.
- [static func inactiveTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride](hovereffectphaseoverride/inactivetemporarily(trigger:).md)
  Temporaily transitions to the inactve phase until all animations finish, and the transition is complete.
- [static func toggled(trigger: some Equatable) -> HoverEffectPhaseOverride](hovereffectphaseoverride/toggled(trigger:).md)
  Immediately transition to the opposite of an effect’s current phase.
- [static func toggledTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride](hovereffectphaseoverride/toggledtemporarily(trigger:).md)
  Temporaily transitions to the opposite of the effect’s current phase at the moment the override is applied.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

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
- [struct OrnamentHoverContentEffect](ornamenthovercontenteffect.md)
  Presents an ornament on hover using a custom effect.
- [struct OrnamentHoverEffect](ornamenthovereffect.md)
  Presents an ornament on hover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride)*