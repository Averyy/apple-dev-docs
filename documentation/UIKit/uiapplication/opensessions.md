# openSessions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The sessions whose scenes are either currently active or archived by the system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var openSessions: Set<UISceneSession> { get }
```

```objc
@property (nonatomic, readonly) NSSet<UISceneSession *> * openSessions;
```

#### Discussion

An archived session doesn’t have a connected scene, but a snapshot of its UI does appear in the app switcher. When the user selects that UI in the app switcher, the system asks your app to recreate the UI from the session information.

## See Also

### Getting scene information
- [var supportsMultipleScenes: Bool](./supportsmultiplescenes.md)
  A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [var connectedScenes: Set<UIScene>](./connectedscenes.md)
  The app’s currently connected scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opensessions)*