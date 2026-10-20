# collectionView(_:writeItemsAt:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Places the data for the drag operation on the pasteboard.

**Availability**:
- macOS 10.11+ - Deprecated in 10.15

> **Deprecated**: Use -collectionView:pasteboardWriterForItemAtIndexPath: instead

## Declaration

```swift
optional func collectionView(_ collectionView: NSCollectionView, writeItemsAt indexPaths: Set<IndexPath>, to pasteboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView writeItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths toPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

[`true`](../../Swift/true.md) if the drag operation can continue or [`false`](../../Swift/false.md) if you want to refuse the drag.

#### Discussion

You must implement this method or the [`collectionView(_:pasteboardWriterForItemAt:)`](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md) method to support drag operations. The collection view calls the [`collectionView(_:pasteboardWriterForItemAt:)`](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md) method in preference to this one if both are implemented. If your app supports multi-image drag and drop, you must implement the [`collectionView(_:pasteboardWriterForItemAt:)`](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md) method.

The collection view calls this method after it has determined that a drag should begin but before the drag operation has started.  Your implementation of this method should do the following:

1. Declare the pasteboard types you support using the [`declareTypes(_:owner:)`](../nspasteboard/declaretypes%28_,owner%29.md) method of the provided `pasteboard` object.
2. Write data to the pasteboard for each type you declare.
3. Return [`true`](../../Swift/true.md) from this method.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The index paths of the items being dragged.
- `pasteboard`: The pasteboard on which to place the drag data.

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
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: Set<IndexPath>) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-6yag4.md)
  Returns the names of the promised files that you created for a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-23ozm)*