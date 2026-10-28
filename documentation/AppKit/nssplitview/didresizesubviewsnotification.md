# didResizeSubviewsNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that posts after a change to the size of some or all subviews of a split view.

**Availability**:
- macOS

## Declaration

```swift
class let didResizeSubviewsNotification: NSNotification.Name
```

```c
extern NSNotificationName NSSplitViewDidResizeSubviewsNotification;
```

## Discussion

The notification object consists of the [`NSSplitView`](../nssplitview.md) that has resized its subviews.

The [`userInfo`](../../Foundation/notification/userinfo.md) dictionary includes the `NSSplitViewDividerIndex` key that contains the index of the divider that the split view or the user moves. If the system sends the notification because the user drags a divider, the dictionary also includes the `NSSplitViewUserResizeKey` key with a value of `1`.

To observe this notification using Swift concurrency, use [`NSSplitView.DidResizeSubviewsMessage`](./didresizesubviewsmessage.md).

## See Also

### Managing Notifications
- [class let willResizeSubviewsNotification: NSNotification.Name](./willresizesubviewsnotification.md)
  A notification that posts before a change to the size of some or all subviews of a split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/didresizesubviewsnotification)*