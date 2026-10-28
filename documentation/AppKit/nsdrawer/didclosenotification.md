# didCloseNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the drawer is closed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
class let didCloseNotification: NSNotification.Name
```

```c
extern NSNotificationName NSDrawerDidCloseNotification;
```

## Discussion

The notification object is the `NSDrawer` object that closed. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications
- [class let didOpenNotification: NSNotification.Name](./didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](./willopennotification.md)
  Posted whenever the drawer is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/didclosenotification)*