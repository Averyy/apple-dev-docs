# NSTableView.DraggingDestinationFeedbackStyle

**Framework**: AppKit  
**Kind**: enum

These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](nstableview/draggingdestinationfeedbackstyle-swift.property.md).

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum DraggingDestinationFeedbackStyle
```

## Topics

### Constants
- [NSTableView.DraggingDestinationFeedbackStyle.none](nstableview/draggingdestinationfeedbackstyle-swift.enum/none.md)
  Provides no feedback when the user drags over the table view. This option exists to allow subclasses to implement their dragging destination highlighting, or to make it not show anything all.
- [NSTableView.DraggingDestinationFeedbackStyle.regular](nstableview/draggingdestinationfeedbackstyle-swift.enum/regular.md)
  Draws a solid round-rect background on drop target rows, and an insertion marker between rows. This style should be used in most cases.
- [NSTableView.DraggingDestinationFeedbackStyle.sourceList](nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist.md)
  Draws an outline on drop target rows, and an insertion marker between rows. This style will automatically be set for source lists when the table’s [`unhideRows(at:withAnimation:)`](nstableview/unhiderows(at:withanimation:).md) is set to [`NSTableView.DraggingDestinationFeedbackStyle.sourceList`](nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist.md). This is the standard look for Source Lists, but may be used in other areas as needed.
- [NSTableView.DraggingDestinationFeedbackStyle.gap](nstableview/draggingdestinationfeedbackstyle-swift.enum/gap.md)
  Provides a gap insertion when dragging over the table. Note that this style is only officially supported for [`NSView`](nsview.md)-based table views, but may partially work in Cell Based TableViews. The decision to use the gap style (compared to another style) can be made in [`tableView(_:draggingSession:willBeginAt:forRowIndexes:)`](nstableviewdatasource/tableview(_:draggingsession:willbeginat:forrowindexes:).md), or it can dynamically be changed.
### Initializers
- [init?(rawValue: Int)](nstableview/draggingdestinationfeedbackstyle-swift.enum/init(rawvalue:).md)

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
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/draggingdestinationfeedbackstyle-swift.enum)*