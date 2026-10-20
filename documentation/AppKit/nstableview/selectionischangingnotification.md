# selectionIsChangingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).

**Availability**:
- macOS

## Declaration

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTableViewSelectionIsChangingNotification;
```

#### Discussion

Note that the notification is sent only for mouse events that change the table’s selection, not keyboard events. The notification object is the table view whose selection is changing. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSTableView.SelectionIsChangingMessage`](./selectionischangingmessage.md).

## See Also

### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](./columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](./columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectionischangingnotification)*