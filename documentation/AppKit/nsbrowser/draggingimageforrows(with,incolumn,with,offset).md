# draggingImageForRows(with:inColumn:with:offset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides an image to represent dragged rows during a drag operation on the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draggingImageForRows(with rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent, offset dragImageOffset: NSPointPointer?) -> NSImage?
```

```objc
- (NSImage *) draggingImageForRowsWithIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column withEvent:(NSEvent *) event offset:(NSPointPointer) dragImageOffset;
```

#### Return Value

Image representing the visible cells identified by rowIndexes.

## Parameters

- `rowIndexes`: Rows the user is dragging.
- `column`: Column with the rows the user is dragging.
- `event`: Mouse drag event.
- `dragImageOffset`: Offset for the returned image:

  - [`NSZeroPoint`](../../Foundation/nszeropoint.md): The image is centered under the pointer.

## See Also

### Related Documentation
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](../nsbrowserdelegate/browser%28_,draggingimageforrowswith,incolumn,with,offset%29.md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
### Dragging
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./candragrows%28with,incolumn,with%29.md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/draggingimageforrows(with:incolumn:with:offset:))*