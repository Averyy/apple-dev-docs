# deselectItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified items from the current selection.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func deselectItems(at indexPaths: Set<IndexPath>)
```

```objc
- (void) deselectItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths;
```

#### Discussion

Use this method to reduce the current selection. If you want to animate the deselection of the new items, call this method on the collection view’s [`animator()`](../nsanimatablepropertycontainer/animator%28%29.md) proxy object instead. This method does not call any methods of the delegate object when making the selection.

## Parameters

- `indexPaths`: The index paths of the items you want to deselect.

## See Also

### Managing the Selection
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [var selectionIndexPaths: Set<IndexPath>](./selectionindexpaths.md)
  The set of index paths representing the currently selected items.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./selectitems%28at,scrollposition%29.md)
  Adds the specified items to the current selection and optionally scrolls the items into position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deselectitems(at:))*