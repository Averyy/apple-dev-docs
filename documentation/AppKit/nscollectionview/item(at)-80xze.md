# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the collection view item for the represented object at the specified index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func item(at index: Int) -> NSCollectionViewItem?
```

```objc
- (NSCollectionViewItem *) itemAtIndex:(NSUInteger) index;
```

## Return Value

An instance of `NSCollectionViewItem`.

## Discussion

Rather than using the [`NSCollectionViewItem`](../nscollectionviewitem.md) instance returned by this method to determine the frame of the collection item’s view you should use [`content`](./content.md), it is significantly more efficient.

## Parameters

- `index`: The index of the collection view item.

## See Also

### Legacy Collection View Support
- [var selectionIndexes: IndexSet](./selectionindexes.md)
  The indexes of the currently selected items.
- [func frameForItem(at: Int) -> NSRect](./frameforitem%28at%29.md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](./frameforitem%28at,withnumberofitems%29.md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./draggingimageforitems%28at,with,offset%29-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/item(at:)-80xze)*