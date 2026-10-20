# columnDidResizeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever a column is resized in an `NSOutlineView` object.

**Availability**:
- macOS

## Declaration

```swift
class let columnDidResizeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSOutlineViewColumnDidResizeNotification;
```

#### Discussion

The notification object is the `NSOutlineView` object in which a column was resized. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSTableColumn"` | The column that was resized. |
| `@"NSOldWidth"` | An [`NSNumber`](../../Foundation/nsnumber.md) object containing the column’s original width |

To observe this notification using Swift concurrency, use [`NSOutlineView.ColumnDidResizeMessage`](./columndidresizemessage.md).

## See Also

### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](./columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](./itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](./itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](./itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](./itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/columndidresizenotification)*