# columnDidResizeNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a column is resized in an `NSTableView` object.

**Availability**:
- macOS ?+

## Declaration

```swift
class let columnDidResizeNotification: NSNotification.Name
```

#### Discussion

The notification object is the table view in which a column was resized. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSTableColumn"` | The column that was resized. |
| `@"NSOldWidth"` | An NSNumber containing the integer value of the column’s original width. |

## See Also

- [class let columnDidMoveNotification: NSNotification.Name](nstableview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](nstableview/selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columndidresizenotification)*