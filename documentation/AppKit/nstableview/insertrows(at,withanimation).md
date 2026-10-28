# insertRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the rows using the specified animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func insertRows(at indexes: IndexSet, withAnimation animationOptions: NSTableView.AnimationOptions = [])
```

```objc
- (void) insertRowsAtIndexes:(NSIndexSet *) indexes withAnimation:(NSTableViewAnimationOptions) animationOptions;
```

## Discussion

The [`numberOfRows`](./numberofrows.md) in the table view is automatically increased by the count of `indexes`.

Calling this method multiple times within the same [`beginUpdates()`](./beginupdates%28%29.md) and [`endUpdates()`](./endupdates%28%29.md) block is allowed, and changes are processed incrementally.

> **Note**:  [`NSCell`](../nscell.md)-based table views must first call [`beginUpdates()`](./beginupdates%28%29.md) before calling this method.

## Parameters

- `indexes`: The final positions of the new rows to be inserted.
- `animationOptions`: The animation displayed during the insert. See [`NSTableView.AnimationOptions`](./animationoptions.md) for the possible values that can be combined using the C bitwise OR operator.

## See Also

### Updating the Table View Arrangement
- [func beginUpdates()](./beginupdates%28%29.md)
  Begins a group of updates for the table view.
- [func endUpdates()](./endupdates%28%29.md)
  Ends the group of updates for the table view.
- [func moveRow(at: Int, to: Int)](./moverow%28at,to%29.md)
  Moves the specified row to the new row location using animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./removerows%28at,withanimation%29.md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](./row%28for%29.md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](./column%28for%29.md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/insertrows(at:withanimation:))*