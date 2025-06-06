# columnDidMoveNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a column is moved by user action in an `NSTableView` object.

**Availability**:
- macOS ?+

## Declaration

```swift
class let columnDidMoveNotification: NSNotification.Name
```

#### Discussion

The notification object is the table view in which a column moved. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldColumn"` | An `NSNumber` object containing the integer value of the column’s original index. |
| `@"NSNewColumn"` | An `NSNumber` object containing the integer value of the column’s present index. |

## See Also

- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [class let columnDidResizeNotification: NSNotification.Name](nstableview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](nstableview/selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columndidmovenotification)*