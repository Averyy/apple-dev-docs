# contextHelpModeDidDeactivateNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the application exits context-sensitive help mode. This happens when the user clicks the mouse button while the cursor is anywhere on the screen after displaying a context-sensitive help topic.

**Availability**:
- macOS

## Declaration

```swift
class let contextHelpModeDidDeactivateNotification: NSNotification.Name
```

```c
extern NSNotificationName NSContextHelpModeDidDeactivateNotification;
```

## Discussion

The notification object is the help manager. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSHelpManager.ContextHelpModeDidDeactivateMessage`](./contexthelpmodediddeactivatemessage.md).

## See Also

### Notifications
- [class let contextHelpModeDidActivateNotification: NSNotification.Name](./contexthelpmodedidactivatenotification.md)
  Posted when the application enters context-sensitive help mode. This typically happens when the user holds down the Help key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelpmodediddeactivatenotification)*