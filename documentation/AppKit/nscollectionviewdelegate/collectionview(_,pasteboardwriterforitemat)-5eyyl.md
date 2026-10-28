# collectionView(_:pasteboardWriterForItemAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides the pasteboard writer for the item at the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, pasteboardWriterForItemAt indexPath: IndexPath) -> (any NSPasteboardWriting)?
```

```objc
- (id<NSPasteboardWriting>) collectionView:(NSCollectionView *) collectionView pasteboardWriterForItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

The pasteboard writer object to use for managing the item data. Return `nil` to prevent the collection view from dragging the item.

## Discussion

You must implement this method or the [`collectionView(_:writeItemsAt:to:)`](./collectionview%28_,writeitemsat,to%29-23ozm.md) method to support drag operations. The collection view calls this method in preference over the [`collectionView(_:writeItemsAt:to:)`](./collectionview%28_,writeitemsat,to%29-23ozm.md) method if both are implemented. If your app supports multi-image drag and drop, you must implement this method.

The collection view calls this method for each item involved in the drag operation after it has determined that a drag should begin but before the drag operation has started.  Your implementation of this method should create and return the pasteboard writer—an object conforming to the [`NSPasteboardWriting`](../nspasteboardwriting.md) protocol—to use for providing the item’s data. Using the object you provide, the collection view creates an [`NSDraggingItem`](../nsdraggingitem.md) object for you and configures its [`draggingFrame`](../nsdraggingitem/draggingframe.md) and [`imageComponents`](../nsdraggingitem/imagecomponents.md) properties for you using information from the item at the specified index path.

If you implement this method, the collection view does not call the [`collectionView(_:draggingImageForItemsAt:with:offset:)`](./collectionview%28_,draggingimageforitemsat,with,offset%29-898js.md) of your delegate or the [`draggingImageForItems(at:with:offset:)`](../nscollectionview/draggingimageforitems%28at,with,offset%29-7rc4k.md) method of [`NSCollectionView`](../nscollectionview.md).

## Parameters

- `collectionView`: The collection view making the request.
- `indexPath`: The index path of the item requiring a pasteboard writer.

## See Also

### Drag and Drop Support
- [Supporting Collection View Drag and Drop Through File Promises](../supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [func collectionView(NSCollectionView, canDragItemsAt: Set<IndexPath>, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-49wix.md)
  Returns a Boolean indicating whether a drag operation involving the specified items can begin.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:pasteboardwriterforitemat:)-5eyyl)*