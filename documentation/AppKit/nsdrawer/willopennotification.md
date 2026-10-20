# willOpenNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the drawer is about to open.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
class let willOpenNotification: NSNotification.Name
```

```c
extern NSNotificationName NSDrawerWillOpenNotification;
```

#### Discussion

The notification object is the `NSDrawer` object about to open. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications
- [class let didCloseNotification: NSNotification.Name](./didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](./didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Posted whenever the drawer is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/willopennotification)*