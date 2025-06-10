# removeRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method

Removes the rows using the specified animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func removeRows(at indexes: IndexSet, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

#### Discussion

This method deletes from the table the rows represented at `indexes` and automatically decreases [`numberOfRows`](nstableview/numberofrows.md) by the count of `indexes`.

The row indexes should be with respect to the current state displayed in the table view, and not the final state, because the specified rows do not exist in the final state.

Calling this method multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md) and [`endUpdates()`](nstableview/endupdates().md) block is allowed, and changes are processed incrementally.

Changes are processed incrementally as the [`insertRows(at:withAnimation:)`](nstableview/insertrows(at:withanimation:).md), [`removeRows(at:withAnimation:)`](nstableview/removerows(at:withanimation:).md), and the [`moveRow(at:to:)`](nstableview/moverow(at:to:).md) methods are called. It is acceptable to delete row `0` multiple times, as long as there is still a row available.

> **Note**:  [`NSCell`](nscell.md)-based table views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

## Parameters

- `indexes`: An index set containing the rows to remove.
- `animationOptions`: The animation displayed during the insert. See   for the possible values that can be combined using the C bitwise OR operator.

## See Also

- [func beginUpdates()](nstableview/beginupdates.md)
  Begins a group of updates for the table view.
- [func endUpdates()](nstableview/endupdates.md)
  Ends the group of updates for the table view.
- [func moveRow(at: Int, to: Int)](nstableview/moverow(at:to:).md)
  Moves the specified row to the new row location using animation.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/insertrows(at:withanimation:).md)
  Inserts the rows using the specified animation.
- [func row(for: NSView) -> Int](nstableview/row(for:).md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](nstableview/column(for:).md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/removerows(at:withanimation:))*