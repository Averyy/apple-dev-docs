# frameForItem(at:withNumberOfItems:)

**Framework**: AppKit  
**Kind**: method

Returns the frame of an item based on the number of items in the collection view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func frameForItem(at index: Int, withNumberOfItems numberOfItems: Int) -> NSRect
```

#### Return Value

The frame rectangle that reflects where the collection view would place the item.

#### Discussion

Using the value in the `numberOfItems` parameter, this method calculates the frame rectangle of the item at the specified `index` in the collection view.

When the collection view is a drag destination, use this method (instead of the [`content`](nscollectionview/content.md) method) to get the frame of items. Drag operations can change the number of items, which affects the layout of the item views.

## Parameters

- `index`: The index of the item in the collection view.
- `numberOfItems`: The targeted number of items in the collection view. Use this parameter to specify the number of items you intend to have in the collection view, if that number is different than the actual number of items.

## See Also

- [var itemPrototype: NSCollectionViewItem?](nscollectionview/itemprototype.md)
  The receiver’s collection view item prototype.
- [func newItem(forRepresentedObject: Any) -> NSCollectionViewItem](nscollectionview/newitem(forrepresentedobject:).md)
  Returns the collection view item that is used for the specified object.
- [var selectionIndexes: IndexSet](nscollectionview/selectionindexes.md)
  The indexes of the currently selected items.
- [var maxNumberOfRows: Int](nscollectionview/maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](nscollectionview/maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var minItemSize: NSSize](nscollectionview/minitemsize.md)
  The minimum size (in points) of items in the collection view grid.
- [var maxItemSize: NSSize](nscollectionview/maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.
- [func item(at: Int) -> NSCollectionViewItem?](nscollectionview/item(at:)-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int) -> NSRect](nscollectionview/frameforitem(at:).md)
  Returns the frame of the collection view item at the specified index.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nscollectionview/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/frameforitem(at:withnumberofitems:))*