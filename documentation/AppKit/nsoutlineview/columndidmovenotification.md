# columnDidMoveNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a column is moved by user action in an `NSOutlineView` object.

**Availability**:
- macOS ?+

## Declaration

```swift
class let columnDidMoveNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSOutlineView` object in which a column moved. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldColumn"` | An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the integer value of the column’s original index |
| `@"NSNewColumn"` | An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the integer value of the column’s present index |

## See Also

- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [class let columnDidResizeNotification: NSNotification.Name](nsoutlineview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](nsoutlineview/itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](nsoutlineview/itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](nsoutlineview/itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](nsoutlineview/itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionDidChangeNotification: NSNotification.Name](nsoutlineview/selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nsoutlineview/selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/columndidmovenotification)*