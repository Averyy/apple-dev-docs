# willChangeStatusBarOrientationNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Posted when the app is about to change the orientation of its interface.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) instead.

## Declaration

```swift
nonisolated
class let willChangeStatusBarOrientationNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationWillChangeStatusBarOrientationNotification;
```

#### Discussion

The userInfo dictionary contains an [`NSNumber`](../../Foundation/nsnumber.md) that encapsulates a `UIInterfaceOrientation` value (see [`UIInterfaceOrientation`](../uiinterfaceorientation.md)). Use [`statusBarOrientationUserInfoKey`](./statusbarorientationuserinfokey.md) to access this value.

## See Also

### Deprecated notifications
- [class let willChangeStatusBarFrameNotification: NSNotification.Name](./willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let didChangeStatusBarFrameNotification: NSNotification.Name](./didchangestatusbarframenotification.md)
  Posted when the frame of the status bar changes.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](./didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/willchangestatusbarorientationnotification)*