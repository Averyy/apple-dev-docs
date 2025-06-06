# NSTableView.RowActionEdge

**Framework**: AppKit  
**Kind**: enum

These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum RowActionEdge
```

## Topics

### Constants
- [NSTableView.RowActionEdge.leading](nstableview/rowactionedge/leading.md)
  Denotes the leading, or left, edge of a table row view.
- [NSTableView.RowActionEdge.trailing](nstableview/rowactionedge/trailing.md)
  Denotes the trailing, or right, edge of a table row view.
### Initializers
- [init?(rawValue: Int)](nstableview/rowactionedge/init(rawvalue:).md)

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
- [NSTableView.DropOperation](nstableview/dropoperation.md)
  `NSTableView` defines these constants to specify drop operations.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowactionedge)*