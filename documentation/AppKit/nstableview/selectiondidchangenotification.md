# selectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after an `NSTableView` object’s selection changes.

**Availability**:
- macOS

## Declaration

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTableViewSelectionDidChangeNotification;
```

#### Discussion

The notification object is the table view whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSTableView.SelectionDidChangeMessage`](./selectiondidchangemessage.md).

## See Also

### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](./columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](./columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectiondidchangenotification)*