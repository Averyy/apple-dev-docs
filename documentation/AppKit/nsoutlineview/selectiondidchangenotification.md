# selectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after the outline view’s selection changes.

**Availability**:
- macOS

## Declaration

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSOutlineViewSelectionDidChangeNotification;
```

## Discussion

The notification object is the outline view whose selection changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSOutlineView.SelectionDidChangeMessage`](./selectiondidchangemessage.md).

## See Also

### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](./columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [class let columnDidResizeNotification: NSNotification.Name](./columndidresizenotification.md)
  Posted whenever a column is resized in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](./itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](./itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](./itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](./itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/selectiondidchangenotification)*