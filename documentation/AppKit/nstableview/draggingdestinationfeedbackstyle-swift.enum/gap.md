# NSTableView.DraggingDestinationFeedbackStyle.gap

**Framework**: AppKit  
**Kind**: case

Provides a gap insertion when dragging over the table. Note that this style is only officially supported for [`NSView`](nsview.md)-based table views, but may partially work in Cell Based TableViews. The decision to use the gap style (compared to another style) can be made in [`tableView(_:draggingSession:willBeginAt:forRowIndexes:)`](nstableviewdatasource/tableview(_:draggingsession:willbeginat:forrowindexes:).md), or it can dynamically be changed.

**Availability**:
- macOS 10.9+

## Declaration

```swift
case gap
```

## See Also

- [NSTableView.DraggingDestinationFeedbackStyle.none](nstableview/draggingdestinationfeedbackstyle-swift.enum/none.md)
  Provides no feedback when the user drags over the table view. This option exists to allow subclasses to implement their dragging destination highlighting, or to make it not show anything all.
- [NSTableView.DraggingDestinationFeedbackStyle.regular](nstableview/draggingdestinationfeedbackstyle-swift.enum/regular.md)
  Draws a solid round-rect background on drop target rows, and an insertion marker between rows. This style should be used in most cases.
- [NSTableView.DraggingDestinationFeedbackStyle.sourceList](nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist.md)
  Draws an outline on drop target rows, and an insertion marker between rows. This style will automatically be set for source lists when the table’s [`unhideRows(at:withAnimation:)`](nstableview/unhiderows(at:withanimation:).md) is set to [`NSTableView.DraggingDestinationFeedbackStyle.sourceList`](nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist.md). This is the standard look for Source Lists, but may be used in other areas as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/draggingdestinationfeedbackstyle-swift.enum/gap)*