# canDragRows(with:inColumn:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func canDragRows(with rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent) -> Bool
```

```objc
- (BOOL) canDragRowsWithIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column withEvent:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) when `rowIndexes` identifies at least one row and all the identified rows are enabled; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `rowIndexes`: Rows the user is dragging
- `column`: Column containing the rows the user is dragging.
- `event`: Mouse-drag event.

## See Also

### Related Documentation
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](../nsbrowserdelegate/browser%28_,candragrowswith,incolumn,with%29.md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
### Dragging
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](./draggingimageforrows%28with,incolumn,with,offset%29.md)
  Provides an image to represent dragged rows during a drag operation on the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/candragrows(with:incolumn:with:))*