# collectionView(_:draggingSession:willBeginAt:forItemsAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies your delegate that a drag session is about to begin.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, draggingSession session: NSDraggingSession, willBeginAt screenPoint: NSPoint, forItemsAt indexes: IndexSet)
```

```objc
- (void) collectionView:(NSCollectionView *) collectionView draggingSession:(NSDraggingSession *) session willBeginAtPoint:(NSPoint) screenPoint forItemsAtIndexes:(NSIndexSet *) indexes;
```

#### Discussion

You can use this method to modify the dragging session or to perform other tasks related to the beginning of a drag session.

## Parameters

- `collectionView`: The collection view notifying your delegate object.
- `session`: The dragging session that is about to begin.
- `screenPoint`: The starting point (in screen coordinates) for the drag operation.
- `indexes`: The indexes of the items being dragged.

## See Also

### Legacy Collection View Support
- [func collectionView(NSCollectionView, canDragItemsAt: IndexSet, with: NSEvent) -> Bool](./collectionview%28_,candragitemsat,with%29-39rjh.md)
  Returns a Boolean indicating whether the collection view can begin dragging the specified items.
- [func collectionView(NSCollectionView, pasteboardWriterForItemAt: Int) -> (any NSPasteboardWriting)?](./collectionview%28_,pasteboardwriterforitemat%29-7ldvs.md)
  Provides the pasteboard writer for the item at the specified index
- [func collectionView(NSCollectionView, writeItemsAt: IndexSet, to: NSPasteboard) -> Bool](./collectionview%28_,writeitemsat,to%29-a1lk.md)
  Invoked after it has been determined that a drag should begin, but before the drag has been started.
- [func collectionView(NSCollectionView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItemsAt: IndexSet) -> [String]](./collectionview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditemsat%29-wwec.md)
  Invoked to return an array of filenames that the receiver promises to create.
- [func collectionView(NSCollectionView, draggingImageForItemsAt: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./collectionview%28_,draggingimageforitemsat,with,offset%29-4yvk5.md)
  Creates and returns a drag image to represent the specified items during a drag.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindex,dropoperation%29.md)
  Validates the specified location to see if it is a valid drop target.
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,index,dropoperation%29.md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:draggingsession:willbeginat:foritemsat:)-cpuq)*