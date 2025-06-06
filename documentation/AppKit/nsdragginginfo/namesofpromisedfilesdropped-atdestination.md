# namesOfPromisedFilesDropped(atDestination:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?
```

#### Return Value

An array of file names, which are not full paths.

#### Discussion

Drag destinations should invoke this method within their performDragOperation: method. The source may or may not have created the files by the time this method returns.

## Parameters

- `dropDestination`: A URL object specifying the drop location for promised files.

## See Also

- [var draggingPasteboard: NSPasteboard](nsdragginginfo/draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](nsdragginginfo/draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](nsdragginginfo/draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](nsdragginginfo/draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingLocation: NSPoint](nsdragginginfo/dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](nsdragginginfo/draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](nsdragginginfo/numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/namesofpromisedfilesdropped(atdestination:))*