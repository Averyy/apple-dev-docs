# beginUpdates()

**Framework**: AppKit  
**Kind**: method

Begins a group of updates for the table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func beginUpdates()
```

#### Discussion

For [`NSView`](nsview.md)-based table views, multiple row changes—that is, insertions, deletions, and moves—are animated simultaneously by surrounding calls to those method calls with [`beginUpdates()`](nstableview/beginupdates().md) and [`endUpdates()`](nstableview/endupdates().md). These methods are nestable.

The selected rows are maintained during the series of insertions, deletions, moves, and scrolling. If a selected row is deleted, a selection changed notification occurs after [`removeRows(at:withAnimation:)`](nstableview/removerows(at:withanimation:).md) is called.

It is not necessary to call [`beginUpdates()`](nstableview/beginupdates().md) and [`endUpdates()`](nstableview/endupdates().md) if only one insertion, deletion, or move is occurring and the table view is an [`NSView`](nsview.md)-based table view. When using an [`NSCell`](nscell.md)-based table view, you must surround any insertion, deletion, or move in an update block for animations to occur.

The main reason for doing a batch update of changes to a table view is to avoid having the table animate unnecessarily.

Note that these methods should be called to reflect changes in your model; they do not make any underlying model changes.

> **Note**:  For [`NSCell`](nscell.md)-based table views, it is required to call [`beginUpdates()`](nstableview/beginupdates().md) if you want to animate the [`insertRows(at:withAnimation:)`](nstableview/insertrows(at:withanimation:).md), [`removeRows(at:withAnimation:)`](nstableview/removerows(at:withanimation:).md), and [`moveRow(at:to:)`](nstableview/moverow(at:to:).md).

 For [`NSCell`](nscell.md)-based table views, it is required to call [`beginUpdates()`](nstableview/beginupdates().md) if you want to animate the [`insertRows(at:withAnimation:)`](nstableview/insertrows(at:withanimation:).md), [`removeRows(at:withAnimation:)`](nstableview/removerows(at:withanimation:).md), and [`moveRow(at:to:)`](nstableview/moverow(at:to:).md).

## See Also

- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [func endUpdates()](nstableview/endupdates.md)
  Ends the group of updates for the table view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/beginupdates())*