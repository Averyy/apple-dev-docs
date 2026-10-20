# collectionView(_:acceptDrop:index:dropOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the mouse is released over a collection view that previously allowed a drop.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, acceptDrop draggingInfo: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView acceptDrop:(id<NSDraggingInfo>) draggingInfo index:(NSInteger) index dropOperation:(NSCollectionViewDropOperation) dropOperation;
```

#### Return Value

[`true`](../../Swift/true.md) if the drop operation should be accepted, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method is called when the mouse is released over a collection view that previously decided to allow a drop via the [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](./collectionview%28_,validatedrop,proposedindex,dropoperation%29.md) method. At this time, the delegate should incorporate the data from the dragging pasteboard and update the collection view’s contents.

You must implement this method for your collection view to be a drag destination

## Parameters

- `collectionView`: The collection view that send the message.
- `draggingInfo`: An object that contains more information about this dragging operation.
- `index`: The index of the proposed drop item.
- `dropOperation`: The type of dragging operation.

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
- [func collectionView(NSCollectionView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItemsAt: IndexSet)](./collectionview%28_,draggingsession,willbeginat,foritemsat%29-cpuq.md)
  Notifies your delegate that a drag session is about to begin.
- [func collectionView(NSCollectionView, validateDrop: any NSDraggingInfo, proposedIndex: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSCollectionView.DropOperation>) -> NSDragOperation](./collectionview%28_,validatedrop,proposedindex,dropoperation%29.md)
  Validates the specified location to see if it is a valid drop target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:))*