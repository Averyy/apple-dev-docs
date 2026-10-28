# UIApplicationSupportsMultipleScenes

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app supports two or more scenes simultaneously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Details

- **Name**: `UIApplicationSupportsMultipleScenes` (Enable Multiple Scenes)
- **Type**: boolean

## Discussion

If your app supports multiple scenes, set the value of this key to [`true`](../../../Swift/true.md). If you set the value to [`false`](../../../Swift/false.md), UIKit never creates more than one scene for your app.

Setting this key to [`true`](../../../Swift/true.md) has implications for your code. An app that supports multiple scenes must coordinate operations to prevent scenes from interfering with each other. For example, if two scenes access the same shared resource, you must synchronize access to that resource using a serial dispatch queue or some other mechanism. Failure to do so may lead to corrupted data or  unexpected behavior from your app.

## See Also

### Multiple windows
- [UIApplicationSupportsTabbedSceneCollection](./uiapplicationsupportstabbedscenecollection.md)
  A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes)*