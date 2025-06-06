# deselectItems(at:)

**Framework**: AppKit  
**Kind**: method

Removes the specified items from the current selection.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func deselectItems(at indexPaths: Set<IndexPath>)
```

#### Discussion

Use this method to reduce the current selection. If you want to animate the deselection of the new items, call this method on the collection view’s [`animator()`](nsanimatablepropertycontainer/animator().md) proxy object instead. This method does not call any methods of the delegate object when making the selection.

## Parameters

- `indexPaths`: The index paths of the items you want to deselect.

## See Also

- [var isSelectable: Bool](nscollectionview/isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](nscollectionview/allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](nscollectionview/allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [var selectionIndexPaths: Set<IndexPath>](nscollectionview/selectionindexpaths.md)
  The set of index paths representing the currently selected items.
- [func selectAll(Any?)](nscollectionview/selectall(_:).md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](nscollectionview/deselectall(_:).md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/selectitems(at:scrollposition:).md)
  Adds the specified items to the current selection and optionally scrolls the items into position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deselectitems(at:))*