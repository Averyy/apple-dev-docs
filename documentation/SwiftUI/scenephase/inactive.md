# ScenePhase.inactive

**Framework**: SwiftUI  
**Kind**: case

The scene is in the foreground but should pause its work.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case inactive
```

#### Discussion

A scene in this phase doesn’t receive events and should pause timers and free any unnecessary resources. The scene might be completely hidden in the user interface or otherwise unavailable to the user. In macOS, scenes only pass through this phase temporarily on their way to the [`ScenePhase.background`](scenephase/background.md) phase.

An app or custom scene in this phase contains no scene instances in the [`ScenePhase.active`](scenephase/active.md) phase.

## See Also

- [ScenePhase.active](scenephase/active.md)
  The scene is in the foreground and interactive.
- [ScenePhase.background](scenephase/background.md)
  The scene isn’t currently visible in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenephase/inactive)*