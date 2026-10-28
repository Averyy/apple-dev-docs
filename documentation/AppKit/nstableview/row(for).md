# row(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the row for the specified view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func row(for view: NSView) -> Int
```

```objc
- (NSInteger) rowForView:(NSView *) view;
```

## Return Value

The index of the row containing to `view`. This method returns `-1` if the view is not in the table view. This method may also return `-1` if the row containing the view is being animated away, such as during the deletion of a row.

## Discussion

This method is typically called in the action method for an `NSButton` (or `NSControl`) to find out what row (and column) the action should be performed on.

The implementation is `O(n)` where *n* is the number of visible rows, so this method should generally not be called within a loop.

## Parameters

- `view`: The view for which to retrieve the row.

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
- [func column(for: NSView) -> Int](./column%28for%29.md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/row(for:))*