# didOpenNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the drawer is opened.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
class let didOpenNotification: NSNotification.Name
```

```c
extern NSNotificationName NSDrawerDidOpenNotification;
```

#### Discussion

The notification object is the `NSDrawer` object that opened. This notification does not contain a `userInfo` dictionary.

## See Also

### Notifications
- [class let didCloseNotification: NSNotification.Name](./didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let willCloseNotification: NSNotification.Name](./willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](./willopennotification.md)
  Posted whenever the drawer is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/didopennotification)*