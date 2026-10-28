# selectionIndexes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The indexes of the currently selected items.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var selectionIndexes: IndexSet { get set }
```

```objc
@property (copy) NSIndexSet * selectionIndexes;
```

## Discussion

Whenever possible, use the [`selectionIndexPaths`](./selectionindexpaths.md) property instead of this one to set selections.

This property is observable using key-value observing.

## See Also

### Legacy Collection View Support
- [func item(at: Int) -> NSCollectionViewItem?](./item%28at%29-80xze.md)
  Returns the collection view item for the represented object at the specified index.
- [func frameForItem(at: Int) -> NSRect](./frameforitem%28at%29.md)
  Returns the frame of the collection view item at the specified index.
- [func frameForItem(at: Int, withNumberOfItems: Int) -> NSRect](./frameforitem%28at,withnumberofitems%29.md)
  Returns the frame of an item based on the number of items in the collection view.
- [func draggingImageForItems(at: IndexSet, with: NSEvent, offset: NSPointPointer) -> NSImage](./draggingimageforitems%28at,with,offset%29-951w7.md)
  This method computes and returns an image to use for dragging.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./setdraggingsourceoperationmask%28_,forlocal%29.md)
  Configures the drag operation mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/selectionindexes)*