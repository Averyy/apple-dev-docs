# collectionView(_:canDragItemsAt:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean indicating whether a drag operation involving the specified items can begin.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, canDragItemsAt indexPaths: Set<IndexPath>, with event: NSEvent) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView canDragItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths withEvent:(NSEvent *) event;
```

## Return Value

[`true`](../../Swift/true.md) if the drag operation can begin or [`false`](../../Swift/false.md) if it cannot.

## Discussion

If you do not implement this method and your collection view has only one section, the collection view calls the legacy [`collectionView(_:canDragItemsAt:with:)`](./collectionview%28_,candragitemsat,with%29-39rjh.md) method. If you do not implement either method, the collection view assumes a return value of [`true`](../../Swift/true.md).

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The index paths of the items about to be dragged.
- `event`: The mouse-down event that began the drag operation.

## See Also

### Drag and Drop Support
- [Supporting Collection View Drag and Drop Through File Promises](../supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: IndexPath) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md)
  Provides the pasteboard writer for the item at the specified index path.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: Set<IndexPath>, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-898js.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: Set<IndexPath>)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-68x2y.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, endedAt: NSPoint, dragOperation: NSDragOperation)](./collectionview%28_,draggingsession,endedat,dragoperation%29.md)
  Notifies your delegate that a drag session ended.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-49wix)*