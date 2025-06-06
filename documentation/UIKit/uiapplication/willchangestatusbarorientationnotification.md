# willChangeStatusBarOrientationNotification

**Framework**: UIKit  
**Kind**: property

Posted when the app is about to change the orientation of its interface.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
nonisolated
class let willChangeStatusBarOrientationNotification: NSNotification.Name
```

#### Discussion

The userInfo dictionary contains an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that encapsulates a `UIInterfaceOrientation` value (see [`UIInterfaceOrientation`](uiinterfaceorientation.md)). Use [`statusBarOrientationUserInfoKey`](uiapplication/statusbarorientationuserinfokey.md) to access this value.

## See Also

- [class let willChangeStatusBarFrameNotification: NSNotification.Name](uiapplication/willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let didChangeStatusBarFrameNotification: NSNotification.Name](uiapplication/didchangestatusbarframenotification.md)
  Posted when the frame of the status bar changes.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](uiapplication/didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/willchangestatusbarorientationnotification)*