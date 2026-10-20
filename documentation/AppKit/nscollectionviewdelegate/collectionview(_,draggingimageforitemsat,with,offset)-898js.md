# collectionView(_:draggingImageForItemsAt:with:offset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a drag image to represent the specified items during a drag.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, draggingImageForItemsAt indexPaths: Set<IndexPath>, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

```objc
- (NSImage *) collectionView:(NSCollectionView *) collectionView draggingImageForItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths withEvent:(NSEvent *) event offset:(NSPointPointer) dragImageOffset;
```

#### Return Value

The image to use for the dragged items.

#### Discussion

Your implementation of this method should create an appropriate image to use during the drag operation.  The collection view places the center of your image at the current mouse location. Update the value in the `dragImageOffset` parameter to shift the position of your image by the specified amount.

If you do not implement this method, the collection view uses the drag image returned by the [`draggingImageForItems(at:with:offset:)`](../nscollectionview/draggingimageforitems%28at,with,offset%29-7rc4k.md) method instead.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The index paths of the items being dragged.
- `event`: The mouse-down event that began the drag operation. You can use the mouse location when determining what value to return in the `dragImageOffset` parameter.
- `dragImageOffset`: The offset value to use when positioning the image. On input, the point is [`NSZeroPoint`](../../Foundation/nszeropoint.md), which centers the returned image under the mouse. Your method can return a different point that repositions the drag image by the specified offset values.

## See Also

### Drag and Drop Support
- [Supporting Collection View Drag and Drop Through File Promises](../supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, canDragItemsAt: Set<IndexPath>, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-49wix.md)
  Returns a Boolean indicating whether a drag operation involving the specified items can begin.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: IndexPath) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-5eyyl.md)
  Provides the pasteboard writer for the item at the specified index path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-898js)*