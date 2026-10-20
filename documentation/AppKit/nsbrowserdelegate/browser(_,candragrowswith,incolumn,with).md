# browser(_:canDragRowsWith:inColumn:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, canDragRowsWith rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) browser canDragRowsWithIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column withEvent:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the drag operation; [`false`](../../Swift/false.md) to disallow it.

## Parameters

- `browser`: The browser.
- `rowIndexes`: The rows the user is dragging.
- `column`: The column containing the rows the user is dragging.
- `event`: The drag event.

## See Also

### Related Documentation
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](../nsbrowser/candragrows%28with,incolumn,with%29.md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
### Dragging
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](./browser%28_,draggingimageforrowswith,incolumn,with,offset%29.md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](./browser%28_,validatedrop,proposedrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](./browser%28_,acceptdrop,atrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](./browser%28_,writerowswith,incolumn,to%29.md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](./browser%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith,incolumn%29.md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:))*