# collectionView(_:draggingSession:endedAt:dragOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies your delegate that a drag session ended.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, draggingSession session: NSDraggingSession, endedAt screenPoint: NSPoint, dragOperation operation: NSDragOperation)
```

```objc
- (void) collectionView:(NSCollectionView *) collectionView draggingSession:(NSDraggingSession *) session endedAtPoint:(NSPoint) screenPoint dragOperation:(NSDragOperation) operation;
```

#### Discussion

You can use this method to perform tasks related to the ending of a drag session.

## Parameters

- `collectionView`: The collection view notifying your delegate object.
- `session`: The dragging session that ended.
- `screenPoint`: The end point (in screen coordinates) for the drag operation.
- `operation`: The operation that was performed. Use this value to determine how the operation ended. For example, for content that was dragged to the trash, the operation type would be [`delete`](../nsdragoperation/delete.md).

## See Also

### Drag and Drop Support
- [Supporting Collection View Drag and Drop Through File Promises](../supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, canDragItemsAt: Set<IndexPath>, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-49wix.md)
  Returns a Boolean indicating whether a drag operation involving the specified items can begin.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: IndexPath) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md)
  Provides the pasteboard writer for the item at the specified index path.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: Set<IndexPath>, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-898js.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: Set<IndexPath>)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-68x2y.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, updateDraggingItemsForDrag: any NSDraggingInfo)](./collectionview%28_,updatedraggingitemsfordrag%29.md)
  Asks your delegate to update the dragging items during a drag operation.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndexPath: AutoreleasingUnsafeMutablePointer<NSIndexPath>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindexpath,dropoperation%29.md)
  Validates whether a drop operation is possible at the specified location.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, indexPath: IndexPath, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,indexpath,dropoperation%29.md)
  Incorporates the dropped content into the collection view.
- [func collectionView(NSCollectionView, writeItemsAt: Set<IndexPath>, to: NSPasteboard) -> Bool](./collectionview%28_,writeitemsat,to%29-23ozm.md)
  Places the data for the drag operation on the pasteboard.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: Set<IndexPath>) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-6yag4.md)
  Returns the names of the promised files that you created for a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:draggingsession:endedat:dragoperation:))*