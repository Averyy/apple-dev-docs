# active

**Framework**: SwiftUI  
**Kind**: property

Immediately transition to the active phase.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var active: HoverEffectPhaseOverride { get }
```

#### Discussion

Applying this override causes a hover effect to become active immediately, regardless of whether the view is hovered or not. The transition will use the animations defined by the effect, but will ignore any delays. The effect remains active until this override is removed.

When applied to a group, all effects in the group become active as well. Applying overrides to multiple effects in the same group is undefined, due to it not being clear which override should be applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/active)*