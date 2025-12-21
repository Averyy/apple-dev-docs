# canDragRows(with:at:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func canDragRows(with rowIndexes: IndexSet, at mouseDownPoint: NSPoint) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) to disallow the drag.

## Parameters

- `rowIndexes`: The row indexes to drag.
- `mouseDownPoint`: The location where the drag was initiated.

## See Also

- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/candragrows(with:at:))*