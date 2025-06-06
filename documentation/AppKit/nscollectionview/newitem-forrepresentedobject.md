# newItem(forRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Returns the collection view item that is used for the specified object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func newItem(forRepresentedObject object: Any) -> NSCollectionViewItem
```

#### Return Value

An initialized collection view item with the specified object and the appropriate view set. The collection view item should not be autoreleased.

#### Discussion

Whenever possible, register classes or nib files for your items instead of using this property. For more information, see Creating Collection View Items.

Subclasses can override this method if the collection view items are not generated from a prototype or if the prototype view needs to be modified. The subclass is responsible for setting the `view`  and representedObject of the new collection view item.

## Parameters

- `object`: The content object that the collection view item will represent.

## See Also

- [var itemPrototype: NSCollectionViewItem?](nscollectionview/itemprototype.md)
  The receiver’s collection view item prototype.
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
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](nscollectionview/frameforitem(at:withnumberofitems:).md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](nscollectionview/draggingimageforitems(at:with:offset:)-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nscollectionview/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the default value returned from [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/newitem(forrepresentedobject:))*