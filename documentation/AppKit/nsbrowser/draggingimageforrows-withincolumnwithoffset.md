# draggingImageForRows(with:inColumn:with:offset:)

**Framework**: AppKit  
**Kind**: method

Provides an image to represent dragged rows during a drag operation on the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func draggingImageForRows(with rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent, offset dragImageOffset: NSPointPointer?) -> NSImage?
```

#### Return Value

Image representing the visible cells identified by rowIndexes.

## Parameters

- `rowIndexes`: Rows the user is dragging.
- `column`: Column with the rows the user is dragging.
- `event`: Mouse drag event.
- `dragImageOffset`: Offset for the returned image:

## See Also

- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:).md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nsbrowser/setdraggingsourceoperationmask(_:forlocal:).md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowser/candragrows(with:incolumn:with:).md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/draggingimageforrows(with:incolumn:with:offset:))*