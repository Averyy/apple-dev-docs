# collectionView(_:writeItemsAt:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked after it has been determined that a drag should begin, but before the drag has been started.

**Availability**:
- macOS 10.6+ - Deprecated in 10.15

> **Deprecated**: Use -collectionView:pasteboardWriterForItemAtIndexPath: instead

## Declaration

```swift
optional func collectionView(_ collectionView: NSCollectionView, writeItemsAt indexes: IndexSet, to pasteboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView writeItemsAtIndexes:(NSIndexSet *) indexes toPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

[`true`](../../Swift/true.md) to begin the drag, otherwise [`false`](../../Swift/false.md).

#### Discussion

To start the drag, you must first declare the pasteboard types that are supported by sending `pasteboard` a [`declareTypes(_:owner:)`](../nspasteboard/declaretypes%28_,owner%29.md) method. You then place the data for the items at the specified indexes on `pasteboard`, and return [`true`](../../Swift/true.md) from the method.

The drag image and other drag related information will be set up and provided by the view once this call returns [`true`](../../Swift/true.md).

You need to implement this method for your collection view to be a drag source.

## Parameters

- `collectionView`: The collection view that send the message.
- `indexes`: The indexes of the items to write to the pasteboard.
- `pasteboard`: The pasteboard containing the content from the dragged items.

## See Also

### Legacy Collection View Support
- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: IndexSet) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-wwec.md)
  Invoked to return an array of filenames that the receiver promises to create.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-4yvk5.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindex,dropoperation%29.md)
  Validates the specified location to see if it is a valid drop target.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,index,dropoperation%29.md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:writeitemsat:to:)-a1lk)*