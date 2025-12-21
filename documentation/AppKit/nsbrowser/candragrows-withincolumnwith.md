# canDragRows(with:inColumn:with:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func canDragRows(with rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when `rowIndexes` identifies at least one row and all the identified rows are enabled; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `rowIndexes`: Rows the user is dragging
- `column`: Column containing the rows the user is dragging.
- `event`: Mouse-drag event.

## See Also

- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:).md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nsbrowser/setdraggingsourceoperationmask(_:forlocal:).md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](nsbrowser/draggingimageforrows(with:incolumn:with:offset:).md)
  Provides an image to represent dragged rows during a drag operation on the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/candragrows(with:incolumn:with:))*