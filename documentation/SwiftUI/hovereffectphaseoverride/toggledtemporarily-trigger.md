# toggledTemporarily(trigger:)

**Framework**: SwiftUI  
**Kind**: method

Temporaily transitions to the opposite of the effect’s current phase at the moment the override is applied.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func toggledTemporarily(trigger: some Equatable) -> HoverEffectPhaseOverride
```

#### Discussion

Use `toggledTemporarily(trigger:)` to toggle an effect’s current phase until it fully transitions to its new phase. The transition will use the animations defined by the effect, but will ignore any delays.

When the override expires, the effect will respond to hover events again. If the view is hovered, the effect will transition to it’s active phase, otherwise its inactive phase.

## Parameters

- `trigger`: A value to observe for changes. The override will be   reapplied whenever this value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectphaseoverride/toggledtemporarily(trigger:))*