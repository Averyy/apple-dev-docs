# clickedRow

**Framework**: AppKit  
**Kind**: property

The index of the row the user clicked.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var clickedRow: Int { get }
```

#### Return Value

The index of the row the user clicked to trigger an action message. Returns `–1` if the user clicked in an area of the table view not occupied by table rows.

#### Discussion

This property contains the index of the row that the user clicked. The value is `-1` when the user clicks in an area of the table view that is not occupied by table rows.

The value of this property is meaningful in the target object’s implementation of the action and double-action methods. You can also use the value to determine which contextual menu to display when the user Control-clicks in a table. Note that you should check to see if `clickedRow` is one of the rows the user selected and if it is, perform the contextual menu operation on all of the selected rows. To see an example of using `clickedRow` in the implementation of a contextual menu, download the [`DragNDropOutlineView: implementing drag and drop in an NSOutlineView`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/DragNDropOutlineView/Introduction/Intro.html#//apple_ref/doc/uid/DTS40008831) sample project.

## See Also

- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var doubleAction: Selector?](nstableview/doubleaction.md)
  The message sent to the table view’s target when the user double-clicks a cell or column header.
- [var clickedColumn: Int](nstableview/clickedcolumn.md)
  The index of the column the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/clickedrow)*