# namesOfPromisedFilesDropped(atDestination:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSFilePromiseReceiver objects instead

## Declaration

```swift
func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?
```

```objc
- (NSArray<NSString *> *) namesOfPromisedFilesDroppedAtDestination:(NSURL *) dropDestination;
```

#### Return Value

An array of file names, which are not full paths.

#### Discussion

Drag destinations should invoke this method within their performDragOperation: method. The source may or may not have created the files by the time this method returns.

## Parameters

- `dropDestination`: A URL object specifying the drop location for promised files.

## See Also

### Obtaining information about the dragging session
- [var draggingPasteboard: NSPasteboard](./draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](./draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](./draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](./draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingLocation: NSPoint](./dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](./draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](./numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/namesofpromisedfilesdropped(atdestination:))*