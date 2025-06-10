# verticalMotionCanBeginDrag

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether vertical motion is treated as a drag or selection change.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var verticalMotionCanBeginDrag: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), which indicates that a vertical drag motion begins a drag. In this case a vertical drag will drag-select rows. Most often, you would want to disable vertical dragging when it’s expected that horizontal dragging is the natural motion.

> **Note**:  Horizontal motion is always a valid motion to begin a drag.

## See Also

- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/verticalmotioncanbegindrag)*