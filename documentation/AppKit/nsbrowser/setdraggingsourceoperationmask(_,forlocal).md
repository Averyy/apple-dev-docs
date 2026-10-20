# setDraggingSourceOperationMask(_:forLocal:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the drag-operation mask for dragging operations with local or external destinations.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDraggingSourceOperationMask(_ mask: NSDragOperation, forLocal isLocal: Bool)
```

```objc
- (void) setDraggingSourceOperationMask:(NSDragOperation) mask forLocal:(BOOL) isLocal;
```

#### Discussion

> ❗ **Important**:  Do not override this method.

## Parameters

- `mask`: Dragging operation mask to use for either local or external drag operations, as specified by localDestination.
- `isLocal`: Indicates the location of the dragging operation’s destination object:

  [`true`](../../Swift/true.md) for this application; [`false`](../../Swift/false.md) for another application.

## See Also

### Dragging
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./candragrows%28with,incolumn,with%29.md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](./draggingimageforrows%28with,incolumn,with,offset%29.md)
  Provides an image to represent dragged rows during a drag operation on the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setdraggingsourceoperationmask(_:forlocal:))*