# endUpdates()

**Framework**: AppKit  
**Kind**: method

Ends the group of updates for the table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func endUpdates()
```

#### Discussion

Ends the group of updates for the table view. This method, like [`beginUpdates()`](nstableview/beginupdates().md), is nestable. See [`beginUpdates()`](nstableview/beginupdates().md) for details.

## See Also

- [func beginUpdates()](nstableview/beginupdates.md)
  Begins a group of updates for the table view.
- [func moveRow(at: Int, to: Int)](nstableview/moverow(at:to:).md)
  Moves the specified row to the new row location using animation.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/insertrows(at:withanimation:).md)
  Inserts the rows using the specified animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/removerows(at:withanimation:).md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](nstableview/row(for:).md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](nstableview/column(for:).md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/endupdates())*