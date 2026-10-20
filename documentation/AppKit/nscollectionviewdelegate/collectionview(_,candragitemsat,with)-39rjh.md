# collectionView(_:canDragItemsAt:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean indicating whether the collection view can begin dragging the specified items.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, canDragItemsAt indexes: IndexSet, with event: NSEvent) -> Bool
```

```objc
- (BOOL) collectionView:(NSCollectionView *) collectionView canDragItemsAtIndexes:(NSIndexSet *) indexes withEvent:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if the collection view can begin the drag operation for the specified items or [`false`](../../Swift/false.md) if it cannot.

#### Discussion

Implement this method when you want selective control over the initiation of drag operations. In your implementation, use the provided information to determine whether the drag operation should occur and return the appropriate return value. For example, you might return [`false`](../../Swift/false.md) if your interface does not allow the user to drag the specified items.

If you do not implement this method in your delegate object, the collection view assumes a return value of [`true`](../../Swift/true.md) and begins the drag operation.

## Parameters

- `collectionView`: The collection view containing the items to be dragged.
- `indexes`: The indexes of the items to be dragged.
- `event`: The mouse event that initiated the drag action.

## See Also

### Legacy Collection View Support
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
- [func collectionView(NSCollectionView, acceptDrop: any NSDraggingInfo, index: Int, dropOperation: NSCollectionView.DropOperation) -> Bool](./collectionview%28_,acceptdrop,index,dropoperation%29.md)
  Invoked when the mouse is released over a collection view that previously allowed a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:candragitemsat:with:)-39rjh)*