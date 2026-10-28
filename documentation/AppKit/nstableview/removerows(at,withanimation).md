# removeRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the rows using the specified animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func removeRows(at indexes: IndexSet, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

```objc
- (void) removeRowsAtIndexes:(NSIndexSet *) indexes withAnimation:(NSTableViewAnimationOptions) animationOptions;
```

## Discussion

This method deletes from the table the rows represented at `indexes` and automatically decreases [`numberOfRows`](./numberofrows.md) by the count of `indexes`.

The row indexes should be with respect to the current state displayed in the table view, and not the final state, because the specified rows do not exist in the final state.

Calling this method multiple times within the same [`beginUpdates()`](./beginupdates%28%29.md) and [`endUpdates()`](./endupdates%28%29.md) block is allowed, and changes are processed incrementally.

Changes are processed incrementally as the [`insertRows(at:withAnimation:)`](./insertrows%28at,withanimation%29.md), [`removeRows(at:withAnimation:)`](./removerows%28at,withanimation%29.md), and the [`moveRow(at:to:)`](./moverow%28at,to%29.md) methods are called. It is acceptable to delete row `0` multiple times, as long as there is still a row available.

> **Note**:  [`NSCell`](../nscell.md)-based table views must first call [`beginUpdates()`](./beginupdates%28%29.md) before calling this method.

## Parameters

- `indexes`: An index set containing the rows to remove.
- `animationOptions`: The animation displayed during the insert. See [`NSTableView.AnimationOptions`](./animationoptions.md) for the possible values that can be combined using the C bitwise OR operator.

## See Also

### Updating the Table View Arrangement
- [func beginUpdates()](./beginupdates%28%29.md)
  Begins a group of updates for the table view.
- [func endUpdates()](./endupdates%28%29.md)
  Ends the group of updates for the table view.
- [func moveRow(at: Int, to: Int)](./moverow%28at,to%29.md)
  Moves the specified row to the new row location using animation.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./insertrows%28at,withanimation%29.md)
  Inserts the rows using the specified animation.
- [func row(for: NSView) -> Int](./row%28for%29.md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](./column%28for%29.md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/removerows(at:withanimation:))*