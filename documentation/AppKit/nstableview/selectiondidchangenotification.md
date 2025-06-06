# selectionDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted after an `NSTableView` object’s selection changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let selectionDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the table view whose selection changed. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let columnDidMoveNotification: NSNotification.Name](nstableview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](nstableview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionIsChangingNotification: NSNotification.Name](nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectiondidchangenotification)*