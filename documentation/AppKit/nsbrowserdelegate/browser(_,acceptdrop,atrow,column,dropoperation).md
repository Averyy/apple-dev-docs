# browser(_:acceptDrop:atRow:column:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate during a dragging session to determine whether to accept the drop.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, acceptDrop info: any NSDraggingInfo, atRow row: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) browser acceptDrop:(id<NSDraggingInfo>) info atRow:(NSInteger) row column:(NSInteger) column dropOperation:(NSBrowserDropOperation) dropOperation;
```

#### Return Value

[`true`](../../Swift/true.md) to accept the drop; [`false`](../../Swift/false.md) to decline it.

#### Discussion

This method is required for a browser to be a drag destination. It is invoked after the [`browser(_:validateDrop:proposedRow:column:dropOperation:)`](./browser%28_,validatedrop,proposedrow,column,dropoperation%29.md) method allows the drop.

The delegate should incorporate the pasteboard data from the dragging session (`info``.draggingPasteboard`).

## Parameters

- `browser`: The browser.
- `info`: The drag session information.
- `row`: The drop row.
- `column`: The drop column.
- `dropOperation`: The drop location relative to `row`.

## See Also

### Dragging
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./browser%28_,candragrowswith,incolumn,with%29.md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](./browser%28_,draggingimageforrowswith,incolumn,with,offset%29.md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](./browser%28_,validatedrop,proposedrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](./browser%28_,writerowswith,incolumn,to%29.md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](./browser%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith,incolumn%29.md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:acceptdrop:atrow:column:dropoperation:))*