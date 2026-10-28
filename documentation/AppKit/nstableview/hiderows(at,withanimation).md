# hideRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Hides the specified table rows.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func hideRows(at indexes: IndexSet, withAnimation rowAnimation: NSTableView.AnimationOptions = [])
```

```objc
- (void) hideRowsAtIndexes:(NSIndexSet *) indexes withAnimation:(NSTableViewAnimationOptions) rowAnimation;
```

## Discussion

Use this method when you no longer want the data to be visible to the user, but you don’t want to permanently remove the data. Hidden table rows have a height of zero and cannot be selected by the user. However, if a selected table row is hidden, it will remain selected.

Hiding a table row causes the [`tableView(_:didRemove:forRow:)`](../nstableviewdelegate/tableview%28_,didremove,forrow%29.md) delegate method to be invoked.

## Parameters

- `indexes`: An index set containing indexes of the rows to be hidden.
- `rowAnimation`: An animation effect to be applied when the rows are hidden.

## See Also

### Related Documentation
- [NSTableView.AnimationOptions](./animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [func tableView(NSTableView, didRemove: NSTableRowView, forRow: Int)](../nstableviewdelegate/tableview%28_,didremove,forrow%29.md)
  Tells the delegate that a row view was removed from the table at the specified row.
### Hiding and Showing Table Rows
- [func unhideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./unhiderows%28at,withanimation%29.md)
  Unhides the specified table rows.
- [var hiddenRowIndexes: IndexSet](./hiddenrowindexes.md)
  The indexes of all hidden table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/hiderows(at:withanimation:))*