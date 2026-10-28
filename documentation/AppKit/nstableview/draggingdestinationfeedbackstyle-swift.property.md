# draggingDestinationFeedbackStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The feedback style displayed when the user drags over the table view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle { get set }
```

```objc
@property NSTableViewDraggingDestinationFeedbackStyle draggingDestinationFeedbackStyle;
```

## Discussion

The default value of this property is [`NSTableView.DraggingDestinationFeedbackStyle.regular`](./draggingdestinationfeedbackstyle-swift.enum/regular.md). However, changing the selection highlight style to [`NSTableView.SelectionHighlightStyle.sourceList`](./selectionhighlightstyle-swift.enum/sourcelist.md) automatically changes the value of this property to [`NSTableView.DraggingDestinationFeedbackStyle.sourceList`](./draggingdestinationfeedbackstyle-swift.enum/sourcelist.md).

## See Also

### Dragging
- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](./dragimageforrows%28with,tablecolumns,event,offset%29.md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](./candragrows%28with,at%29.md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](./verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](./setdroprow%28_,dropoperation%29.md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/draggingdestinationfeedbackstyle-swift.property)*