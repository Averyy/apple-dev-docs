# NSTableView.ColumnAutoresizingStyle

**Framework**: AppKit  
**Kind**: enum

The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](nstableview/columnautoresizingstyle-swift.property.md) property.

**Availability**:
- macOS ?+

## Declaration

```swift
enum ColumnAutoresizingStyle
```

## Topics

### Constants
- [NSTableView.ColumnAutoresizingStyle.noColumnAutoresizing](nstableview/columnautoresizingstyle-swift.enum/nocolumnautoresizing.md)
  Disable table column autoresizing.
- [NSTableView.ColumnAutoresizingStyle.uniformColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/uniformcolumnautoresizingstyle.md)
  Autoresize all columns by distributing space equally, simultaneously.
- [NSTableView.ColumnAutoresizingStyle.sequentialColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/sequentialcolumnautoresizingstyle.md)
  Autoresize each table column sequentially, from the last auto-resizable column to the first auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.
- [NSTableView.ColumnAutoresizingStyle.reverseSequentialColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/reversesequentialcolumnautoresizingstyle.md)
  Autoresize each table column sequentially, from the first auto-resizable column to the last auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.
- [NSTableView.ColumnAutoresizingStyle.lastColumnOnlyAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/lastcolumnonlyautoresizingstyle.md)
  Autoresize only the last table column.
- [NSTableView.ColumnAutoresizingStyle.firstColumnOnlyAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/firstcolumnonlyautoresizingstyle.md)
  Autoresize only the first table column.
### Initializers
- [init?(rawValue: UInt)](nstableview/columnautoresizingstyle-swift.enum/init(rawvalue:).md)

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
- [NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](nstableview/selectionhighlightstyle-swift.property.md) property.
- [NSTableView.AnimationOptions](nstableview/animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](nstableview/effectiverowsizestyle.md) and [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](nstablecellview.md) class’ property [`rowSizeStyle`](nstablecellview/rowsizestyle.md).
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columnautoresizingstyle-swift.enum)*