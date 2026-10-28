# moveRow(at:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the specified row to the new row location using animation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func moveRow(at oldIndex: Int, to newIndex: Int)
```

```objc
- (void) moveRowAtIndex:(NSInteger) oldIndex toIndex:(NSInteger) newIndex;
```

## Discussion

This is similar to removing a row at `oldIndex` and inserting it at `newIndex`, except the same view is used and simply has its position updated to the new location.

Changes happen incrementally as they are sent to the table, so as soon as this method is called the row can be considered moved. However the underlying view is not moved until [`endUpdates()`](./endupdates%28%29.md) has been called.

This method can be called multiple times within the same [`beginUpdates()`](./beginupdates%28%29.md) and [`endUpdates()`](./endupdates%28%29.md) block.

> **Note**:  [`NSCell`](../nscell.md)-based table views must first call [`beginUpdates()`](./beginupdates%28%29.md) before calling this method.

## Parameters

- `oldIndex`: Initial row index.
- `newIndex`: New row index.

## See Also

### Updating the Table View Arrangement
- [func beginUpdates()](./beginupdates%28%29.md)
  Begins a group of updates for the table view.
- [func endUpdates()](./endupdates%28%29.md)
  Ends the group of updates for the table view.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./insertrows%28at,withanimation%29.md)
  Inserts the rows using the specified animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./removerows%28at,withanimation%29.md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](./row%28for%29.md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](./column%28for%29.md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/moverow(at:to:))*