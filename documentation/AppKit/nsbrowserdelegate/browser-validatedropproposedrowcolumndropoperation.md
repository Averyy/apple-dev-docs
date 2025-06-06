# browser(_:validateDrop:proposedRow:column:dropOperation:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, validateDrop info: any NSDraggingInfo, proposedRow row: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation
```

#### Return Value

The drag operation that the data source is to perform. For the browser to accept the drop, it must not be [`NSDragOperationNone`](nsdragoperation/nsdragoperationnone.md).

#### Discussion

The browser proposes a drop column, row, and row-relative location for the drop based on the pointer position, as shown in this table:

| Drop relative location | Description |
| --- | --- |
| [`NSBrowser.DropOperation.on`](nsbrowser/dropoperation/on.md) | Dragging location (`dragInfo``.draggingLocation`) is closer to the middle of `row` than to either of its vertical sides. |
| [`NSBrowser.DropOperation.above`](nsbrowser/dropoperation/above.md) | Dragging location is between two rows. Indicates a drop location above `row` and below `row` `- 1`. |

These are a few examples of how to specify a drop location:

|  | Row index | Row-relative location |
| --- | --- | --- |
| On row 2 | `2` | [`NSBrowser.DropOperation.on`](nsbrowser/dropoperation/on.md) |
| Between rows 2 and 3 | `3` | [`NSBrowser.DropOperation.above`](nsbrowser/dropoperation/above.md) |
| Below the last row | `[sender numberOfRows]` | [`NSBrowser.DropOperation.above`](nsbrowser/dropoperation/above.md) |
| All rows | `-1` | [`NSBrowser.DropOperation.on`](nsbrowser/dropoperation/on.md) |

## Parameters

- `browser`: The browser.
- `info`: The drag session information.
- `row`: On input, the proposed drop row. On output, the drop row.
- `column`: On input, the proposed drop column. On output, the drop column.
- `dropOperation`: On input, the proposed drop location. On output, the drop location.

## See Also

- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:).md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:).md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](nsbrowserdelegate/browser(_:acceptdrop:atrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](nsbrowserdelegate/browser(_:writerowswith:incolumn:to:).md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](nsbrowserdelegate/browser(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:incolumn:).md)
  Implements file promise drag operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:validatedrop:proposedrow:column:dropoperation:))*