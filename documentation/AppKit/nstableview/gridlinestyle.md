# NSTableView.GridLineStyle

**Framework**: AppKit  
**Kind**: struct

`NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](nstableview/gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.

**Availability**:
- macOS ?+

## Declaration

```swift
struct GridLineStyle
```

## Topics

### Constants
- [static var solidVerticalGridLineMask: NSTableView.GridLineStyle](nstableview/gridlinestyle/solidverticalgridlinemask.md)
  Specifies that vertical grid lines should be displayed.
- [static var solidHorizontalGridLineMask: NSTableView.GridLineStyle](nstableview/gridlinestyle/solidhorizontalgridlinemask.md)
  Specifies that horizontal grid lines should be displayed.
- [static var dashedHorizontalGridLineMask: NSTableView.GridLineStyle](nstableview/gridlinestyle/dashedhorizontalgridlinemask.md)
  Specifies that the horizontal grid lines should be drawn dashed.
### Initializers
- [init(rawValue: UInt)](nstableview/gridlinestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Specifying a Custom Row View in a Nib File](specifying-a-custom-row-view-in-a-nib-file.md)
  View-based table view instances use `NSTableViewRowKey` to identify the nib file containing the template row view. You can specify a custom row view (without any code) by associating this key with the appropriate nib name in Interface Builder.
- [NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.enum.md)
  These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](nstableview/draggingdestinationfeedbackstyle-swift.property.md).
- [NSTableView.DropOperation](nstableview/dropoperation.md)
  `NSTableView` defines these constants to specify drop operations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/gridlinestyle)*