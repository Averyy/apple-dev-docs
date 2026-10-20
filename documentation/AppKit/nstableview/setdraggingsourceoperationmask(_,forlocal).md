# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.

**Availability**:
- macOS

## Declaration

```swift
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

```objc
- (void) setDraggingSourceOperationMask:(NSDragOperation) mask forLocal:(BOOL) isLocal;
```

## Parameters

- `mask`: The drag operation mask. See [`NSDragOperation`](../nsdragoperation.md) for the supported values.
- `isLocal`: [`true`](../../Swift/true.md) if the destination is the same application, otherwise [`false`](../../Swift/false.md). In either case the specified `mask` value is archived and used.

## See Also

### Dragging
- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](./dragimageforrows%28with,tablecolumns,event,offset%29.md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](./candragrows%28with,at%29.md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [var verticalMotionCanBeginDrag: Bool](./verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](./setdroprow%28_,dropoperation%29.md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setdraggingsourceoperationmask(_:forlocal:))*