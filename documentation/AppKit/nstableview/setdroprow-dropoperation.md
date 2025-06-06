# setDropRow(_:dropOperation:)

**Framework**: AppKit  
**Kind**: method

Retargets the proposed drop operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setDropRow(_ row: Int, dropOperation: NSTableView.DropOperation)
```

#### Discussion

For example, to specify a drop on the second row, specify `row` as 1, and `operation` as `NSTableViewDropOn`. To specify a drop below the last row, specify `row` as `[self numberOfRows]` and `operation` as `NSTableViewDropAbove`.

Passing a value of `–1` for `row` and `NSTableViewDropOn` as the `operation` causes the entire table view to be highlighted rather than a specific row. This is useful if the data displayed by the table view does not allow the user to drop items at a specific row location.

## Parameters

- `row`: The target row index.
- `dropOperation`: The drop operation. Supported values are specified by  .

## See Also

- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setdroprow(_:dropoperation:))*