# inactiveTemporarily(trigger:)

**Framework**: SwiftUI  
**Kind**: method

Temporaily transitions to the inactve phase until all animations finish, and the transition is complete.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func inactiveTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride
```

#### Discussion

Use `inactiveTemporarily(trigger:)` to override an effect’s phase until it fully transitions to its inactive phase. The transition will use the animations defined by the effect, but will ignore any delays.

When the override expires, the effect will respond to hover events again. If the view isn’t hovered, the effect will remain in the inactive phase. Otherwise it will begin transitioning to the active phase, honoring any delays defined on the effect.

When applied to a group, all effects in the group become inactive as well. Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.

## Parameters

- `trigger`: A value to observe for changes. The override will be   reapplied whenever this value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/inactivetemporarily(trigger:))*