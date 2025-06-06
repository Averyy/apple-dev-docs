# selectionIsChangingNotification

**Framework**: AppKit  
**Kind**: property

Posted as the outline view’s selection changes (while the mouse button is still down).

**Availability**:
- macOS ?+

## Declaration

```swift
class let selectionIsChangingNotification: NSNotification.Name
```

#### Discussion

The notification object is the outline view whose selection is changing. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let columnDidMoveNotification: NSNotification.Name](nsoutlineview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/selectionischangingnotification)*