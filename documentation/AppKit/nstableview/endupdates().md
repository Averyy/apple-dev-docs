# endUpdates()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Ends the group of updates for the table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func endUpdates()
```

```objc
- (void) endUpdates;
```

## Discussion

Ends the group of updates for the table view. This method, like [`beginUpdates()`](./beginupdates%28%29.md), is nestable. See [`beginUpdates()`](./beginupdates%28%29.md) for details.

## See Also

### Updating the Table View Arrangement
- [func beginUpdates()](./beginupdates%28%29.md)
  Begins a group of updates for the table view.
- [func moveRow(at: Int, to: Int)](./moverow%28at,to%29.md)
  Moves the specified row to the new row location using animation.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./insertrows%28at,withanimation%29.md)
  Inserts the rows using the specified animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./removerows%28at,withanimation%29.md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](./row%28for%29.md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](./column%28for%29.md)
  Returns the column index for the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/endupdates())*