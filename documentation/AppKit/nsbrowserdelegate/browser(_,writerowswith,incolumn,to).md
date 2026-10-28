# browser(_:writeRowsWith:inColumn:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.

**Availability**:
- macOS 10.5+ - Deprecated in 27.0

> **Deprecated**: Use browser:pasteboardWriterForRow:column: instead

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, writeRowsWith rowIndexes: IndexSet, inColumn column: Int, to pasteboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) browser writeRowsWithIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column toPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

[`true`](../../Swift/true.md) to allow the dragging operation to proceed (see discussion for further details); [`false`](../../Swift/false.md) to disallow it.

## Discussion

This method is called after a drag operation has been allowed to start ([`browser(_:canDragRowsWith:inColumn:with:)`](./browser%28_,candragrowswith,incolumn,with%29.md) returns [`true`](../../Swift/true.md)), but before it actually begins.

## Parameters

- `browser`: The browser.
- `rowIndexes`: The indexes of the rows the user is dragging.
- `column`: The index of the column containing the dragged rows.
- `pasteboard`: The pasteboard containing the content from the dragged rows.

## See Also

### Dragging
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./browser%28_,candragrowswith,incolumn,with%29.md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](./browser%28_,draggingimageforrowswith,incolumn,with,offset%29.md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](./browser%28_,validatedrop,proposedrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](./browser%28_,acceptdrop,atrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](./browser%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith,incolumn%29.md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:writerowswith:incolumn:to:))*