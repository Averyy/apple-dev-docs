# collectionView(_:namesOfPromisedFilesDroppedAtDestination:forDraggedItemsAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to return an array of filenames that the receiver promises to create.

**Availability**:
- macOS 10.6+ - Deprecated in 10.13

> **Deprecated**: Use NSFilePromiseReceiver objects instead

## Declaration

```swift
optional func collectionView(_ collectionView: NSCollectionView, namesOfPromisedFilesDroppedAtDestination dropURL: URL, forDraggedItemsAt indexes: IndexSet) -> [String]
```

```objc
- (NSArray<NSString *> *) collectionView:(NSCollectionView *) collectionView namesOfPromisedFilesDroppedAtDestination:(NSURL *) dropURL forDraggedItemsAtIndexes:(NSIndexSet *) indexes;
```

#### Return Value

An array of filenames (not full paths) for the created files that the receiver promises to create.

#### Discussion

The delegate can support file promise drags by adding NSFilesPromisePboardType to the pasteboard in [`collectionView(_:writeItemsAt:to:)`](./collectionview%28_,writeitemsat,to%29-a1lk.md).

For more information on file promise dragging, see documentation for the NSDraggingSource protocol and [`namesOfPromisedFilesDropped(atDestination:)`](../nsdragginginfo/namesofpromisedfilesdropped%28atdestination%29.md).

You do not need to implement this delegate method for your collection view to be a drag source.

## Parameters

- `collectionView`: The collection view that send the message.
- `dropURL`: The drop location where the files are created.
- `indexes`: The indexes of the dragging items.

## See Also

### Legacy Collection View Support
- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
- [func collectionView(NSCollectionView, writeItemsAt: IndexSet, to: NSPasteboard) -> Bool](./collectionview%28_,writeitemsat,to%29-a1lk.md)
  Invoked after it has been determined that a drag should begin, but before the drag has been started.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-4yvk5.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindex,dropoperation%29.md)
  Validates the specified location to see if it is a valid drop target.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,index,dropoperation%29.md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:namesofpromisedfilesdroppedatdestination:fordraggeditemsat:)-wwec)*