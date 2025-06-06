# unhideRows(at:withAnimation:)

**Framework**: AppKit  
**Kind**: method

Unhides the specified table rows.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func unhideRows(at indexes: IndexSet, withAnimation rowAnimation: NSTableView.AnimationOptions = [])
```

#### Discussion

Unhiding a table row causes the [`tableView(_:didAdd:forRow:)`](nstableviewdelegate/tableview(_:didadd:forrow:).md) delegate method to be invoked.

## Parameters

- `indexes`: An index set containing indexes of the hidden rows to be shown again.
- `rowAnimation`: An animation effect to be applied when the rows are hidden.

## See Also

- [NSTableView.AnimationOptions](nstableview/animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [func tableView(NSTableView, didAdd: NSTableRowView, forRow: Int)](nstableviewdelegate/tableview(_:didadd:forrow:).md)
  Tells the delegate that a row view was added at the specified row.
- [func hideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/hiderows(at:withanimation:).md)
  Hides the specified table rows.
- [var hiddenRowIndexes: IndexSet](nstableview/hiddenrowindexes.md)
  The indexes of all hidden table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/unhiderows(at:withanimation:))*