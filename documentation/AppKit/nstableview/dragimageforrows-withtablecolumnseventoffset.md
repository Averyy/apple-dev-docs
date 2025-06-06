# dragImageForRows(with:tableColumns:event:offset:)

**Framework**: AppKit  
**Kind**: method

Computes and returns an image to use for dragging.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dragImageForRows(with dragRows: IndexSet, tableColumns: [NSTableColumn], event dragEvent: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

#### Return Value

An `NSImage` containing a custom image for the specified rows and columns participating in the drag.

## Parameters

- `dragRows`: An index set containing the row indexes that should be in the image.
- `tableColumns`: An array of table columns that should be in the image.
- `dragEvent`: The event that initiated the drag.
- `dragImageOffset`: An in/out parameter specifying the offset of the cursor in the image, the default value is  . Returning   causes the cursor to be centered.

## See Also

- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/dragimageforrows(with:tablecolumns:event:offset:))*