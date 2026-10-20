# NSTableView.AnimationOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Specifies the animation effects to apply when inserting or removing rows.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct AnimationOptions
```

```c
enum NSTableViewAnimationOptions : NSUInteger;
```

## Topics

### Constants
- [static var effectFade: NSTableView.AnimationOptions](./animationoptions/effectfade.md)
  Use a fade for row or column removal. The effect can be combined with any of the slide constants.
- [static var effectGap: NSTableView.AnimationOptions](./animationoptions/effectgap.md)
  Creates a gap for newly inserted rows. This is useful for drag and drop animations that animate to a newly opened gap and should be used in the delegate method [`tableView(_:acceptDrop:row:dropOperation:)`](../nstableviewdatasource/tableview%28_,acceptdrop,row,dropoperation%29.md).
- [static var slideUp: NSTableView.AnimationOptions](./animationoptions/slideup.md)
  Animates a row insertion or removal by sliding upward.
- [static var slideDown: NSTableView.AnimationOptions](./animationoptions/slidedown.md)
  Animates a row insertion or removal by sliding downward.
- [static var slideLeft: NSTableView.AnimationOptions](./animationoptions/slideleft.md)
  Animates a row insertion by sliding from the left. Animates a row removal by sliding towards the left.
- [static var slideRight: NSTableView.AnimationOptions](./animationoptions/slideright.md)
  Animates a row insertion by sliding from the right. Animates a row removal by sliding towards the right.
### Initializers
- [init(rawValue: UInt)](./animationoptions/init%28rawvalue%29.md)

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
- [NSTableView.GridLineStyle](./gridlinestyle.md)
  `NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](./gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](../nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.
- [NSTableView.ColumnAutoresizingStyle](./columnautoresizingstyle-swift.enum.md)
  The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](./columnautoresizingstyle-swift.property.md) property.
- [NSTableView.SelectionHighlightStyle](./selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](./selectionhighlightstyle-swift.property.md) property.
- [NSTableView.RowSizeStyle](./rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](./effectiverowsizestyle.md) and [`rowSizeStyle`](./rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](../nstablecellview.md) class’ property [`rowSizeStyle`](../nstablecellview/rowsizestyle.md).
- [NSTableView.RowActionEdge](./rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/animationoptions)*