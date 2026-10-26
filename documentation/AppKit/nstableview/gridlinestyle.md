# NSTableView.GridLineStyle

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

`NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](./gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](../nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.

**Availability**:
- macOS

## Declaration

```swift
struct GridLineStyle
```

```c
enum NSTableViewGridLineStyle : NSUInteger;
```

## Topics

### Constants
- [static var solidVerticalGridLineMask: NSTableView.GridLineStyle](./gridlinestyle/solidverticalgridlinemask.md)
  Specifies that vertical grid lines should be displayed.
- [static var solidHorizontalGridLineMask: NSTableView.GridLineStyle](./gridlinestyle/solidhorizontalgridlinemask.md)
  Specifies that horizontal grid lines should be displayed.
- [static var dashedHorizontalGridLineMask: NSTableView.GridLineStyle](./gridlinestyle/dashedhorizontalgridlinemask.md)
  Specifies that the horizontal grid lines should be drawn dashed.
- [NSTableViewGridNone](../nstableviewgridlinestyle/nstableviewgridnone.md)
  Specifies that no grid lines should be displayed.
### Initializers
- [init(rawValue: UInt)](./gridlinestyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [Specifying a Custom Row View in a Nib File](../specifying-a-custom-row-view-in-a-nib-file.md)
  View-based table view instances use `NSTableViewRowKey` to identify the nib file containing the template row view. You can specify a custom row view (without any code) by associating this key with the appropriate nib name in Interface Builder.
- [NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.enum.md)
  These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](./draggingdestinationfeedbackstyle-swift.property.md).
- [NSTableView.DropOperation](./dropoperation.md)
  `NSTableView` defines these constants to specify drop operations.
- [NSTableView.ColumnAutoresizingStyle](./columnautoresizingstyle-swift.enum.md)
  The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](./columnautoresizingstyle-swift.property.md) property.
- [NSTableView.SelectionHighlightStyle](./selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](./selectionhighlightstyle-swift.property.md) property.
- [NSTableView.AnimationOptions](./animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [NSTableView.RowSizeStyle](./rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](./effectiverowsizestyle.md) and [`rowSizeStyle`](./rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](../nstablecellview.md) class’ property [`rowSizeStyle`](../nstablecellview/rowsizestyle.md).
- [NSTableView.RowActionEdge](./rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/gridlinestyle)*