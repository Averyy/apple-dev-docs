# moveRow(at:to:)

**Framework**: AppKit  
**Kind**: method

Moves the specified row to the new row location using animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func moveRow(at oldIndex: Int, to newIndex: Int)
```

#### Discussion

This is similar to removing a row at `oldIndex` and inserting it at `newIndex`, except the same view is used and simply has its position updated to the new location.

Changes happen incrementally as they are sent to the table, so as soon as this method is called the row can be considered moved. However the underlying view is not moved until [`endUpdates()`](nstableview/endupdates().md) has been called.

This method can be called multiple times within the same [`beginUpdates()`](nstableview/beginupdates().md) and [`endUpdates()`](nstableview/endupdates().md) block.

> **Note**:  [`NSCell`](nscell.md)-based table views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

 [`NSCell`](nscell.md)-based table views must first call [`beginUpdates()`](nstableview/beginupdates().md) before calling this method.

## Parameters

- `oldIndex`: Initial row index.
- `newIndex`: New row index.

## See Also

- [func beginUpdates()](nstableview/beginupdates.md)
  Begins a group of updates for the table view.
- [func endUpdates()](nstableview/endupdates.md)
  Ends the group of updates for the table view.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/insertrows(at:withanimation:).md)
  Inserts the rows using the specified animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/removerows(at:withanimation:).md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](nstableview/row(for:).md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](nstableview/column(for:).md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/moverow(at:to:))*