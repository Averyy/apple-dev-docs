# willResizeSubviewsNotification

**Framework**: AppKit  
**Kind**: property

A notification that posts before a change to the size of some or all subviews of a split view.

**Availability**:
- macOS ?+

## Declaration

```swift
class let willResizeSubviewsNotification: NSNotification.Name
```

#### Discussion

The notification object consists of the [`NSSplitView`](nssplitview.md) object about to resize its subviews.

The [`userInfo`](https://developer.apple.com/documentation/Foundation/Notification/userInfo) dictionary includes the `NSSplitViewDividerIndex` key that contains the index of the divider that the split view or the user moves. If the system sends the notification because the user drags a divider, the dictionary also includes the `NSSplitViewUserResizeKey` key with a value of `1`.

## See Also

- [class let didResizeSubviewsNotification: NSNotification.Name](nssplitview/didresizesubviewsnotification.md)
  A notification that posts after a change to the size of some or all subviews of a split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/willresizesubviewsnotification)*