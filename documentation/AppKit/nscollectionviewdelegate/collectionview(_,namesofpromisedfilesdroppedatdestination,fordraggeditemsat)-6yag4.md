# collectionView(_:namesOfPromisedFilesDroppedAtDestination:forDraggedItemsAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the names of the promised files that you created for a drag operation.

**Availability**:
- macOS 10.11+ - Deprecated in 10.13

> **Deprecated**: Use NSFilePromiseReceiver objects instead

## Declaration

```swift
optional func collectionView(_ collectionView: NSCollectionView, namesOfPromisedFilesDroppedAtDestination dropURL: URL, forDraggedItemsAt indexPaths: Set<IndexPath>) -> [String]
```

```objc
- (NSArray<NSString *> *) collectionView:(NSCollectionView *) collectionView namesOfPromisedFilesDroppedAtDestination:(NSURL *) dropURL forDraggedItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths;
```

#### Return Value

An array of strings containing the filenames you created, or intend to create, at the specified URL.

#### Discussion

At the start of a drag operation, your app must provide the data that constitutes the items being dragged. If you specify a file promise, instead of the data itself, use this method to specify the names of the files you promised. If the files already exist, move them to the directory specified by the `dropURL` parameter. If you must create the files first, use this method to specify the names of the files you intend to provide and begin creating those files asynchronously on a background thread.

The filenames you return are made available from the [`namesOfPromisedFilesDropped(atDestination:)`](../nsdragginginfo/namesofpromisedfilesdropped%28atdestination%29.md) method of the [`NSDraggingInfo`](../nsdragginginfo.md) object passed around during the drag operation.

For more information about how to use file promises when dragging content, see [Drag and Drop Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i).

## Parameters

- `collectionView`: The collection view asking you to provide the list of filenames.
- `dropURL`: The URL at which to create the promised files.
- `indexPaths`: The index paths of the dragged items.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:namesofpromisedfilesdroppedatdestination:fordraggeditemsat:)-6yag4)*