# connectedScenes

**Framework**: UIKit  
**Kind**: property

The app’s currently connected scenes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var connectedScenes: Set<UIScene> { get }
```

#### Discussion

Connected scenes are those that are in memory and potentially doing active work. A connected scene may be in the foreground or background, and it may be onscreen or offscreen.

## See Also

- [var supportsMultipleScenes: Bool](uiapplication/supportsmultiplescenes.md)
  A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [var openSessions: Set<UISceneSession>](uiapplication/opensessions.md)
  The sessions whose scenes are either currently active or archived by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/connectedscenes)*