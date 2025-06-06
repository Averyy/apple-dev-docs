# insertRows(at:withAnimation:)

**Framework**: Appkit  
**Kind**: method

Inserts the rows using the specified animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func insertRows(at indexes: IndexSet, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

#### Discussion

The [`numberOfRows`](nstableview/numberofrows.md) in the table view is automatically increased by the count of `indexes`.

Calling this method multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md) and [`endUpdates()`](nstableview/endupdates().md) block is allowed, and changes are processed incrementally.

> **Note**:  [`NSCell`](nscell.md)-based table views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

## Parameters

- `indexes`: The final positions of the new rows to be inserted.
- `animationOptions`: The animation displayed during the insert. See   for the possible values that can be combined using the C bitwise OR operator.

## See Also

- [func beginUpdates()](nstableview/beginupdates.md)
  Begins a group of updates for the table view.
- [func endUpdates()](nstableview/endupdates.md)
  Ends the group of updates for the table view.
- [func moveRow(at: Int, to: Int)](nstableview/moverow(at:to:).md)
  Moves the specified row to the new row location using animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/removerows(at:withanimation:).md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](nstableview/row(for:).md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](nstableview/column(for:).md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/insertrows(at:withanimation:))*