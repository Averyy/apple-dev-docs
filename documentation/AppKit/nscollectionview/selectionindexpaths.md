# selectionIndexPaths

**Framework**: AppKit  
**Kind**: property

The set of index paths representing the currently selected items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var selectionIndexPaths: Set<IndexPath> { get set }
```

#### Discussion

This property reflects the index paths of the currently selected items, where each index path contains a [`section`](https://developer.apple.com/documentation/Foundation/NSIndexPath/section) number and an index number for the [`item`](https://developer.apple.com/documentation/Foundation/NSIndexPath/item) in that section. This property is updated automatically when the user selects items interactively. You can also change the selection programmatically by assigning a new value to this property. To animate changes to the selection, call this method on the collection view’s [`animator()`](nsanimatablepropertycontainer/animator().md) proxy object instead.

It is a programmer error to specify an index path that does not refer to a valid item in the data source. If you specify an invalid index path, this method raises an exception.

This property is key-value observable. Other methods that modify the selection automatically update this property.

## See Also

- [var isSelectable: Bool](nscollectionview/isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](nscollectionview/allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](nscollectionview/allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [func selectAll(Any?)](nscollectionview/selectall(_:).md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](nscollectionview/deselectall(_:).md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/selectitems(at:scrollposition:).md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](nscollectionview/deselectitems(at:).md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/selectionindexpaths)*