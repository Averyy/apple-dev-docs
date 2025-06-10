# NSTableView.RowSizeStyle

**Framework**: AppKit  
**Kind**: enum

The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](nstableview/effectiverowsizestyle.md) and [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](nstablecellview.md) class’ property [`rowSizeStyle`](nstablecellview/rowsizestyle.md).

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum RowSizeStyle
```

## Topics

### Constants
- [NSTableView.RowSizeStyle.default](nstableview/rowsizestyle-swift.enum/default.md)
  The table will use the system default layout size: small, medium or large.
- [NSTableView.RowSizeStyle.custom](nstableview/rowsizestyle-swift.enum/custom.md)
  The table will use the [`rowHeight`](nstableview/rowheight.md) or invoke the delegate method [`tableView(_:heightOfRow:)`](nstableviewdelegate/tableview(_:heightofrow:).md), if implemented. The cell layout is not changed.
- [NSTableView.RowSizeStyle.small](nstableview/rowsizestyle-swift.enum/small.md)
  The table will use a row height specified for a small table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.
- [NSTableView.RowSizeStyle.medium](nstableview/rowsizestyle-swift.enum/medium.md)
  The table will use a row height specified for a medium table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.
- [NSTableView.RowSizeStyle.large](nstableview/rowsizestyle-swift.enum/large.md)
  The table will use a row height specified for a large table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.
### Initializers
- [init?(rawValue: Int)](nstableview/rowsizestyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle-swift.enum)*