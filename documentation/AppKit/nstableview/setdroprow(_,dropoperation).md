# setDropRow(_:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Retargets the proposed drop operation.

**Availability**:
- macOS

## Declaration

```swift
func setDropRow(_ row: Int, dropOperation: NSTableView.DropOperation)
```

```objc
- (void) setDropRow:(NSInteger) row dropOperation:(NSTableViewDropOperation) dropOperation;
```

#### Discussion

For example, to specify a drop on the second row, specify `row` as 1, and `operation` as `NSTableViewDropOn`. To specify a drop below the last row, specify `row` as `[self numberOfRows]` and `operation` as `NSTableViewDropAbove`.

Passing a value of `–1` for `row` and `NSTableViewDropOn` as the `operation` causes the entire table view to be highlighted rather than a specific row. This is useful if the data displayed by the table view does not allow the user to drop items at a specific row location.

## Parameters

- `row`: The target row index.
- `dropOperation`: The drop operation. Supported values are specified by [`NSTableView.DropOperation`](./dropoperation.md).

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
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setdroprow(_:dropoperation:))*