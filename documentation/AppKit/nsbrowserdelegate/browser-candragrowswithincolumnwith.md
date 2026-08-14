# browser(_:canDragRowsWith:inColumn:with:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, canDragRowsWith rowIndexes: IndexSet, inColumn column: Int, with event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to allow the drag operation; [`false`](https://developer.apple.com/documentation/swift/false) to disallow it.

## Parameters

- `browser`: The browser.
- `rowIndexes`: The rows the user is dragging.
- `column`: The column containing the rows the user is dragging.
- `event`: The drag event.

## See Also

- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowser/candragrows(with:incolumn:with:).md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:).md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](nsbrowserdelegate/browser(_:validatedrop:proposedrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](nsbrowserdelegate/browser(_:acceptdrop:atrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](nsbrowserdelegate/browser(_:writerowswith:incolumn:to:).md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](nsbrowserdelegate/browser(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:incolumn:).md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:))*