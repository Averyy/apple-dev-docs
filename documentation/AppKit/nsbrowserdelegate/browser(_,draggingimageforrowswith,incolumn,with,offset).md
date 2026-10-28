# browser(_:draggingImageForRowsWith:inColumn:with:offset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, draggingImageForRowsWith rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage?
```

```objc
- (NSImage *) browser:(NSBrowser *) browser draggingImageForRowsWithIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column withEvent:(NSEvent *) event offset:(NSPointPointer) dragImageOffset;
```

## Return Value

An image representing the visible rows identified by `rowIndexes`.

## Parameters

- `browser`: The browser.
- `rowIndexes`: The indexes of the rows the user is dragging.
- `column`: The column containing the rows the user is dragging.
- `event`: The drag event.
- `dragImageOffset`: The offset for the returned image:

  - [`NSZeroPoint`](../../Foundation/nszeropoint.md): Centers the image under the pointer.

## See Also

### Related Documentation
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](../nsbrowser/draggingimageforrows%28with,incolumn,with,offset%29.md)
  Provides an image to represent dragged rows during a drag operation on the browser.
### Dragging
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./browser%28_,candragrowswith,incolumn,with%29.md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](./browser%28_,validatedrop,proposedrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](./browser%28_,acceptdrop,atrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](./browser%28_,writerowswith,incolumn,to%29.md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](./browser%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith,incolumn%29.md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:))*