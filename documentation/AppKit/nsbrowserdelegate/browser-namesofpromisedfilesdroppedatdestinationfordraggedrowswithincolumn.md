# browser(_:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWith:inColumn:)

**Framework**: AppKit  
**Kind**: method

Implements file promise drag operations.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func browser(_ browser: NSBrowser, namesOfPromisedFilesDroppedAtDestination dropDestination: URL, forDraggedRowsWith rowIndexes: IndexSet, inColumn column: Int) -> [String]
```

#### Return Value

Filenames (not pathnames) for the actual files represented by the rows the user is dropping.

#### Discussion

Note that file promise drag operation support requires adding the data type [`filePromise`](nspasteboard/pasteboardtype/filepromise.md) to the pasteboard in the [`browser(_:writeRowsWith:inColumn:to:)`](nsbrowserdelegate/browser(_:writerowswith:incolumn:to:).md) method.

## Parameters

- `browser`: The browser.
- `dropDestination`: The drop filesystem location.
- `rowIndexes`: The indexes of the rows the user is dropping.
- `column`: The index of the column containing the rows the user is dropping.

## See Also

- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:).md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:).md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](nsbrowserdelegate/browser(_:validatedrop:proposedrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](nsbrowserdelegate/browser(_:acceptdrop:atrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](nsbrowserdelegate/browser(_:writerowswith:incolumn:to:).md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:incolumn:))*