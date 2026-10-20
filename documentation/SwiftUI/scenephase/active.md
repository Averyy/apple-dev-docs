# ScenePhase.active

**Framework**: SwiftUI  
**Kind**: case  
**Role**: Case

The scene is in the foreground and interactive.

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
case active
```

#### Discussion

An active scene isn’t necessarily front-most. For example, a macOS window might be active even if it doesn’t currently have focus. Nevertheless, all scenes should operate normally in this phase.

An app or custom scene in this phase contains at least one active scene instance.

## See Also

### Getting scene phases
- [ScenePhase.inactive](./inactive.md)
  The scene is in the foreground but should pause its work.
- [ScenePhase.background](./background.md)
  The scene isn’t currently visible in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenephase/active)*