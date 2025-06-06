# NSTableView.DropOperation

**Framework**: AppKit  
**Kind**: enum

`NSTableView` defines these constants to specify drop operations.

**Availability**:
- macOS ?+

## Declaration

```swift
enum DropOperation
```

#### Overview

For example, given a table with `n` rows (numbered with row `0` at the top visually), a row of `n–1` and operation of `NSTableViewDropOn` would specify a drop on the last row. To specify a drop below the last row, you use a row of `n` and `NSTableViewDropAbove` for the operation.

## Topics

### Constants
- [NSTableView.DropOperation.on](nstableview/dropoperation/on.md)
  Specifies that the drop should occur on the specified row.
- [NSTableView.DropOperation.above](nstableview/dropoperation/above.md)
  Specifies that the drop should occur above the specified row.
- [NSTableView.DropOperation.on](nstableview/dropoperation/on.md)
  Specifies that the drop should occur on the specified row.
- [NSTableView.DropOperation.above](nstableview/dropoperation/above.md)
  Specifies that the drop should occur above the specified row.
### Initializers
- [init?(rawValue: UInt)](nstableview/dropoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Specifying a Custom Row View in a Nib File](specifying-a-custom-row-view-in-a-nib-file.md)
  View-based table view instances use `NSTableViewRowKey` to identify the nib file containing the template row view. You can specify a custom row view (without any code) by associating this key with the appropriate nib name in Interface Builder.
- [NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.enum.md)
  These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](nstableview/draggingdestinationfeedbackstyle-swift.property.md).
- [NSTableView.GridLineStyle](nstableview/gridlinestyle.md)
  `NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](nstableview/gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.
- [NSTableView.ColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum.md)
  The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](nstableview/columnautoresizingstyle-swift.property.md) property.
- [NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](nstableview/selectionhighlightstyle-swift.property.md) property.
- [NSTableView.AnimationOptions](nstableview/animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](nstableview/effectiverowsizestyle.md) and [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](nstablecellview.md) class’ property [`rowSizeStyle`](nstablecellview/rowsizestyle.md).
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/dropoperation)*