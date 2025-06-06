# selectItems(at:scrollPosition:)

**Framework**: AppKit  
**Kind**: method

Adds the specified items to the current selection and optionally scrolls the items into position.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func selectItems(at indexPaths: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)
```

#### Discussion

Use this method to extend the current selection. If you want to animate the selection of the new items, call this method on the collection view’s [`animator()`](nsanimatablepropertycontainer/animator().md) proxy object instead. This method does not call any methods of the delegate object when making the selection.

## Parameters

- `indexPaths`: The index paths of the items you want to select.
- `scrollPosition`: The options for scrolling the newly selected items into view. You may combine one vertical and one horizontal scrolling option when calling this method. Specifying more than one option for either the vertical or horizontal directions raises an exception.

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
- [func deselectItems(at: Set<IndexPath>)](nscollectionview/deselectitems(at:).md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/selectitems(at:scrollposition:))*