# openSessions

**Framework**: UIKit  
**Kind**: property

The sessions whose scenes are either currently active or archived by the system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var openSessions: Set<UISceneSession> { get }
```

#### Discussion

An archived session doesn’t have a connected scene, but a snapshot of its UI does appear in the app switcher. When the user selects that UI in the app switcher, the system asks your app to recreate the UI from the session information.

## See Also

- [var supportsMultipleScenes: Bool](uiapplication/supportsmultiplescenes.md)
  A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [var connectedScenes: Set<UIScene>](uiapplication/connectedscenes.md)
  The app’s currently connected scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opensessions)*