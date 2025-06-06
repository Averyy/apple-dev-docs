# ScenePhase.background

**Framework**: SwiftUI  
**Kind**: case

The scene isn’t currently visible in the UI.

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
case background
```

#### Discussion

Do as little as possible in a scene that’s in the `background` phase. The `background` phase can precede termination, so do any cleanup work immediately upon entering this state. For example, close any open files and network connections. However, a scene can also return to the [`ScenePhase.active`](scenephase/active.md) phase from the background.

Expect an app that enters the `background` phase to terminate.

## See Also

- [ScenePhase.active](scenephase/active.md)
  The scene is in the foreground and interactive.
- [ScenePhase.inactive](scenephase/inactive.md)
  The scene is in the foreground but should pause its work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenephase/background)*