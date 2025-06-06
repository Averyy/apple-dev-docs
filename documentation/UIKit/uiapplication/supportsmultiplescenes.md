# supportsMultipleScenes

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the app may display multiple scenes simultaneously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportsMultipleScenes: Bool { get }
```

#### Discussion

UIKit sets this property to [`true`](https://developer.apple.com/documentation/swift/true) when the system allows the app to display multiple scenes and the app’s `Info.plist` file includes the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) key with a value of [`true`](https://developer.apple.com/documentation/swift/true). If either of those conditions isn’t true, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

Use the [`connectedScenes`](uiapplication/connectedscenes.md) property to determine whether multiple scenes are present.

## See Also

- [var connectedScenes: Set<UIScene>](uiapplication/connectedscenes.md)
  The app’s currently connected scenes.
- [var openSessions: Set<UISceneSession>](uiapplication/opensessions.md)
  The sessions whose scenes are either currently active or archived by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/supportsmultiplescenes)*