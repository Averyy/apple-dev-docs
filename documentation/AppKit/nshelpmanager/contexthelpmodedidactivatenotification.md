# contextHelpModeDidActivateNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.

**Availability**:
- macOS

## Declaration

```swift
class let contextHelpModeDidActivateNotification: NSNotification.Name
```

```c
extern NSNotificationName NSContextHelpModeDidActivateNotification;
```

#### Discussion

The notification object is the help manager. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSHelpManager.ContextHelpModeDidActivateMessage`](./contexthelpmodedidactivatemessage.md).

## See Also

### Notifications
- [class let contextHelpModeDidDeactivateNotification: NSNotification.Name](./contexthelpmodediddeactivatenotification.md)
  Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelpmodedidactivatenotification)*