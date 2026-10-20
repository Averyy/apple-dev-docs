# NSTableView.DraggingDestinationFeedbackStyle.sourceList

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Draws an outline on drop target rows, and an insertion marker between rows. This style will automatically be set for source lists when the table’s [`unhideRows(at:withAnimation:)`](../unhiderows%28at,withanimation%29.md) is set to [`NSTableView.DraggingDestinationFeedbackStyle.sourceList`](./sourcelist.md). This is the standard look for Source Lists, but may be used in other areas as needed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
case sourceList
```

```c
NSTableViewDraggingDestinationFeedbackStyleSourceList
```

## See Also

### Constants
- [NSTableView.DraggingDestinationFeedbackStyle.none](./none.md)
  Provides no feedback when the user drags over the table view. This option exists to allow subclasses to implement their dragging destination highlighting, or to make it not show anything all.
- [NSTableView.DraggingDestinationFeedbackStyle.regular](./regular.md)
  Draws a solid round-rect background on drop target rows, and an insertion marker between rows. This style should be used in most cases.
- [NSTableView.DraggingDestinationFeedbackStyle.gap](./gap.md)
  Provides a gap insertion when dragging over the table. Note that this style is only officially supported for [`NSView`](../../nsview.md)-based table views, but may partially work in Cell Based TableViews. The decision to use the gap style (compared to another style) can be made in [`tableView(_:draggingSession:willBeginAt:forRowIndexes:)`](../../nstableviewdatasource/tableview%28_,draggingsession,willbeginat,forrowindexes%29.md), or it can dynamically be changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist)*