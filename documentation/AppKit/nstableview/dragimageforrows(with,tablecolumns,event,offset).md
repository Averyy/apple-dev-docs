# dragImageForRows(with:tableColumns:event:offset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Computes and returns an image to use for dragging.

**Availability**:
- macOS

## Declaration

```swift
func dragImageForRows(with dragRows: IndexSet, tableColumns: [NSTableColumn], event dragEvent: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

```objc
- (NSImage *) dragImageForRowsWithIndexes:(NSIndexSet *) dragRows tableColumns:(NSArray<NSTableColumn *> *) tableColumns event:(NSEvent *) dragEvent offset:(NSPointPointer) dragImageOffset;
```

## Return Value

An `NSImage` containing a custom image for the specified rows and columns participating in the drag.

## Parameters

- `dragRows`: An index set containing the row indexes that should be in the image.
- `tableColumns`: An array of table columns that should be in the image.
- `dragEvent`: The event that initiated the drag.
- `dragImageOffset`: An in/out parameter specifying the offset of the cursor in the image, the default value is [`NSZeroPoint`](../../Foundation/nszeropoint.md). Returning [`NSZeroPoint`](../../Foundation/nszeropoint.md) causes the cursor to be centered.

## See Also

### Dragging
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](./candragrows%28with,at%29.md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](./verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](./setdroprow%28_,dropoperation%29.md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/dragimageforrows(with:tablecolumns:event:offset:))*