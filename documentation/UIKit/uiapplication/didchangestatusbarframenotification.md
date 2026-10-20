# didChangeStatusBarFrameNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Posted when the frame of the status bar changes.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) instead.

## Declaration

```swift
nonisolated
class let didChangeStatusBarFrameNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationDidChangeStatusBarFrameNotification;
```

#### Discussion

The `userInfo` dictionary contains an [`NSValue`](../../Foundation/nsvalue.md) object that encapsulates a [`CGRect`](../../CoreFoundation/cgrect.md) structure expressing the location and size of the new status bar frame. Use [`statusBarFrameUserInfoKey`](./statusbarframeuserinfokey.md) to access this value.

## See Also

### Deprecated notifications
- [class let willChangeStatusBarFrameNotification: NSNotification.Name](./willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let willChangeStatusBarOrientationNotification: NSNotification.Name](./willchangestatusbarorientationnotification.md)
  Posted when the app is about to change the orientation of its interface.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](./didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didchangestatusbarframenotification)*