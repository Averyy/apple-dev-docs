# itemWillExpandNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).

**Availability**:
- macOS

## Declaration

```swift
class let itemWillExpandNotification: NSNotification.Name
```

```c
extern NSNotificationName NSOutlineViewItemWillExpandNotification;
```

## Discussion

The notification object is the outline view that contains an item about to be expanded. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSObject"` | The item that is to be expanded (an `id`) |

To observe this notification using Swift concurrency, use [`NSOutlineView.ItemWillExpandMessage`](./itemwillexpandmessage.md).

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
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/itemwillexpandnotification)*