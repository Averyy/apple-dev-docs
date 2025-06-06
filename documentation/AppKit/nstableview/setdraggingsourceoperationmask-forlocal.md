# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

## Parameters

- `mask`: The drag operation mask. See   for the supported values.
- `isLocal`:   if the destination is the same application, otherwise  . In either case the specified   value is archived and used.

## See Also

- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setdraggingsourceoperationmask(_:forlocal:))*