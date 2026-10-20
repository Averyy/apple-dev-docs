# columnDidMoveNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever a column is moved by user action in an `NSOutlineView` object.

**Availability**:
- macOS

## Declaration

```swift
class let columnDidMoveNotification: NSNotification.Name
```

```c
extern NSNotificationName NSOutlineViewColumnDidMoveNotification;
```

#### Discussion

The notification object is the `NSOutlineView` object in which a column moved. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldColumn"` | An [`NSNumber`](../../Foundation/nsnumber.md) object containing the integer value of the column’s original index |
| `@"NSNewColumn"` | An [`NSNumber`](../../Foundation/nsnumber.md) object containing the integer value of the column’s present index |

## See Also

### Related Documentation
- [func moveColumn(Int, toColumn: Int)](../nstableview/movecolumn%28_,tocolumn%29.md)
  Moves the column and heading at the specified index to the new specified index.
### Notifications
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
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](./selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/columndidmovenotification)*