# didChangeStatusBarFrameNotification

**Framework**: UIKit  
**Kind**: property

Posted when the frame of the status bar changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
nonisolated
class let didChangeStatusBarFrameNotification: NSNotification.Name
```

#### Discussion

The `userInfo` dictionary contains an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object that encapsulates a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) structure expressing the location and size of the new status bar frame. Use [`statusBarFrameUserInfoKey`](uiapplication/statusbarframeuserinfokey.md) to access this value.

## See Also

- [class let willChangeStatusBarFrameNotification: NSNotification.Name](uiapplication/willchangestatusbarframenotification.md)
  Posted when the app is about to change the frame of the status bar.
- [class let willChangeStatusBarOrientationNotification: NSNotification.Name](uiapplication/willchangestatusbarorientationnotification.md)
  Posted when the app is about to change the orientation of its interface.
- [class let didChangeStatusBarOrientationNotification: NSNotification.Name](uiapplication/didchangestatusbarorientationnotification.md)
  Posted when the orientation of the app’s user interface changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didchangestatusbarframenotification)*