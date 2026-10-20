# NSTableView.RowActionEdge

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum RowActionEdge
```

```c
enum NSTableRowActionEdge : NSInteger;
```

## Topics

### Constants
- [NSTableView.RowActionEdge.leading](./rowactionedge/leading.md)
  Denotes the leading, or left, edge of a table row view.
- [NSTableView.RowActionEdge.trailing](./rowactionedge/trailing.md)
  Denotes the trailing, or right, edge of a table row view.
### Initializers
- [init?(rawValue: Int)](./rowactionedge/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Specifying a Custom Row View in a Nib File](../specifying-a-custom-row-view-in-a-nib-file.md)
  View-based table view instances use `NSTableViewRowKey` to identify the nib file containing the template row view. You can specify a custom row view (without any code) by associating this key with the appropriate nib name in Interface Builder.
- [NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.enum.md)
  These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](./draggingdestinationfeedbackstyle-swift.property.md).
- [NSTableView.DropOperation](./dropoperation.md)
  `NSTableView` defines these constants to specify drop operations.
- [NSTableView.GridLineStyle](./gridlinestyle.md)
  `NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](./gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](../nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.
- [NSTableView.ColumnAutoresizingStyle](./columnautoresizingstyle-swift.enum.md)
  The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](./columnautoresizingstyle-swift.property.md) property.
- [NSTableView.SelectionHighlightStyle](./selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](./selectionhighlightstyle-swift.property.md) property.
- [NSTableView.AnimationOptions](./animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [NSTableView.RowSizeStyle](./rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](./effectiverowsizestyle.md) and [`rowSizeStyle`](./rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](../nstablecellview.md) class’ property [`rowSizeStyle`](../nstablecellview/rowsizestyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowactionedge)*