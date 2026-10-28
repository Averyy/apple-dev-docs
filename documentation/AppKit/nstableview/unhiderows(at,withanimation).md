# unhideRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unhides the specified table rows.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func unhideRows(at indexes: IndexSet, withAnimation rowAnimation: NSTableView.AnimationOptions = [])
```

```objc
- (void) unhideRowsAtIndexes:(NSIndexSet *) indexes withAnimation:(NSTableViewAnimationOptions) rowAnimation;
```

## Discussion

Unhiding a table row causes the [`tableView(_:didAdd:forRow:)`](../nstableviewdelegate/tableview%28_,didadd,forrow%29.md) delegate method to be invoked.

## Parameters

- `indexes`: An index set containing indexes of the hidden rows to be shown again.
- `rowAnimation`: An animation effect to be applied when the rows are hidden.

## See Also

### Related Documentation
- [NSTableView.AnimationOptions](./animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [func tableView(NSTableView, didAdd: NSTableRowView, forRow: Int)](../nstableviewdelegate/tableview%28_,didadd,forrow%29.md)
  Tells the delegate that a row view was added at the specified row.
### Hiding and Showing Table Rows
- [func hideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](./hiderows%28at,withanimation%29.md)
  Hides the specified table rows.
- [var hiddenRowIndexes: IndexSet](./hiddenrowindexes.md)
  The indexes of all hidden table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/unhiderows(at:withanimation:))*