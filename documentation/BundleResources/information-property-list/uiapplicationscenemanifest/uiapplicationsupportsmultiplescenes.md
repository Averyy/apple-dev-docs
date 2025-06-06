# UIApplicationSupportsMultipleScenes

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether the app supports two or more scenes simultaneously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

#### Discussion

If your app supports multiple scenes, set the value of this key to [`true`](https://developer.apple.com/documentation/swift/true). If you set the value to [`false`](https://developer.apple.com/documentation/swift/false), UIKit never creates more than one scene for your app.

Setting this key to [`true`](https://developer.apple.com/documentation/swift/true) has implications for your code. An app that supports multiple scenes must coordinate operations to prevent scenes from interfering with each other. For example, if two scenes access the same shared resource, you must synchronize access to that resource using a serial dispatch queue or some other mechanism. Failure to do so may lead to corrupted data or  unexpected behavior from your app.

## See Also

- [UIApplicationSupportsTabbedSceneCollection](information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md)
  A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes)*