# draggingImageForItems(at:with:offset:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This method computes and returns an image to use for dragging.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func draggingImageForItems(at indexes: IndexSet, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

```objc
- (NSImage *) draggingImageForItemsAtIndexes:(NSIndexSet *) indexes withEvent:(NSEvent *) event offset:(NSPointPointer) dragImageOffset;
```

#### Return Value

An image containing a rendering of the visible portions of the views for each item.

#### Discussion

You can override the default image by subclassing NSCollectionView and overriding this method, or by implementing the [`collectionView(_:draggingImageForItemsAt:with:offset:)`](../nscollectionviewdelegate/collectionview%28_,draggingimageforitemsat,with,offset%29-4yvk5.md) delegate method, it will be preferred over this method.

## Parameters

- `indexes`: The index set of the items to be dragged.
- `event`: Mouse drag event.
- `dragImageOffset`: An in/out parameter that will initially be set to [`NSZeroPoint`](../../Foundation/nszeropoint.md). it can be modified to reposition the returned image. A `dragImageOffset` of [`NSZeroPoint`](../../Foundation/nszeropoint.md) will cause the image to be centered under the mouse.

## See Also

### Legacy Collection View Support
- [var selectionIndexes: IndexSet](./selectionindexes.md)
  The indexes of the currently selected items.
- [func item(at: Int) -> NSCollectionViewItem?](./item%28at%29-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int) -> NSRect](./frameforitem%28at%29.md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](./frameforitem%28at,withnumberofitems%29.md)
  Returns the frame of an item based on the number of items in the collection view.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/draggingimageforitems(at:with:offset:)-951w7)*