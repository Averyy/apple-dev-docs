# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method

Specifies the drag-operation mask for dragging operations with local or external destinations.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

#### Discussion

> ❗ **Important**:  Do not override this method.

## Parameters

- `mask`: Dragging operation mask to use for either local or external drag operations, as specified by localDestination.
- `isLocal`:  for this application;   for another application.

## See Also

- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowser/candragrows(with:incolumn:with:).md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](nsbrowser/draggingimageforrows(with:incolumn:with:offset:).md)
  Provides an image to represent dragged rows during a drag operation on the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setdraggingsourceoperationmask(_:forlocal:))*