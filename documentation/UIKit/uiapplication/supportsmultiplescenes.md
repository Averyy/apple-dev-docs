# supportsMultipleScenes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app may display multiple scenes simultaneously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var supportsMultipleScenes: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsMultipleScenes;
```

#### Discussion

UIKit sets this property to [`true`](../../Swift/true.md) when the system allows the app to display multiple scenes and the app’s `Info.plist` file includes the [`UIApplicationSupportsMultipleScenes`](../../BundleResources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) key with a value of [`true`](../../Swift/true.md). If either of those conditions isn’t true, the value of this property is [`false`](../../Swift/false.md).

Use the [`connectedScenes`](./connectedscenes.md) property to determine whether multiple scenes are present.

## See Also

### Getting scene information
- [var connectedScenes: Set<UIScene>](./connectedscenes.md)
  The app’s currently connected scenes.
- [var openSessions: Set<UISceneSession>](./opensessions.md)
  The sessions whose scenes are either currently active or archived by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/supportsmultiplescenes)*