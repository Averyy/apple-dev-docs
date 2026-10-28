# canDragRows(with:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.

**Availability**:
- macOS

## Declaration

```swift
func canDragRows(with rowIndexes: IndexSet, at mouseDownPoint: NSPoint) -> Bool
```

```objc
- (BOOL) canDragRowsWithIndexes:(NSIndexSet *) rowIndexes atPoint:(NSPoint) mouseDownPoint;
```

## Return Value

[`false`](../../Swift/false.md) to disallow the drag.

## Parameters

- `rowIndexes`: The row indexes to drag.
- `mouseDownPoint`: The location where the drag was initiated.

## See Also

### Dragging
- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](./dragimageforrows%28with,tablecolumns,event,offset%29.md)
  Computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](./verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](./setdroprow%28_,dropoperation%29.md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/candragrows(with:at:))*