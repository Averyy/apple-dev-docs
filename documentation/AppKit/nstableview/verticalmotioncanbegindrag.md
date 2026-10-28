# verticalMotionCanBeginDrag

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether vertical motion is treated as a drag or selection change.

**Availability**:
- macOS

## Declaration

```swift
var verticalMotionCanBeginDrag: Bool { get set }
```

```objc
@property BOOL verticalMotionCanBeginDrag;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which indicates that a vertical drag motion begins a drag. In this case a vertical drag will drag-select rows. Most often, you would want to disable vertical dragging when it’s expected that horizontal dragging is the natural motion.

> **Note**:  Horizontal motion is always a valid motion to begin a drag.

## See Also

### Dragging
- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](./dragimageforrows%28with,tablecolumns,event,offset%29.md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](./candragrows%28with,at%29.md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](./setdroprow%28_,dropoperation%29.md)
  Retargets the proposed drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/verticalmotioncanbegindrag)*