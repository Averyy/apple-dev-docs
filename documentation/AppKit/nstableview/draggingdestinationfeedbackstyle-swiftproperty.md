# draggingDestinationFeedbackStyle

**Framework**: AppKit  
**Kind**: property

The feedback style displayed when the user drags over the table view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle { get set }
```

#### Discussion

The default value of this property is [`NSTableView.DraggingDestinationFeedbackStyle.regular`](nstableview/draggingdestinationfeedbackstyle-swift.enum/regular.md). However, changing the selection highlight style to [`NSTableView.SelectionHighlightStyle.sourceList`](nstableview/selectionhighlightstyle-swift.enum/sourcelist.md) automatically changes the value of this property to [`NSTableView.DraggingDestinationFeedbackStyle.sourceList`](nstableview/draggingdestinationfeedbackstyle-swift.enum/sourcelist.md).

## See Also

- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/draggingdestinationfeedbackstyle-swift.property)*