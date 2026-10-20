# column(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the column index for the specified view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func column(for view: NSView) -> Int
```

```objc
- (NSInteger) columnForView:(NSView *) view;
```

#### Return Value

The index of the column containing `view` in the [`tableColumns`](./tablecolumns.md) array. This method returns `-1` if the view is not in the table view. This method may also return `-1` if the row containing the view is being animated away, such as during the deletion of a row.

#### Discussion

This method is typically called in the action method of an `NSButton` (or `NSControl`) to find out what row (and column) the action should be performed on.

The implementation is `O(n)` where *n* is the number of visible rows, so this method should generally not be called within a loop.

## Parameters

- `view`: The view for which to retrieve the column.

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
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./removerows%28at,withanimation%29.md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](./row%28for%29.md)
  Returns the index of the row for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/column(for:))*