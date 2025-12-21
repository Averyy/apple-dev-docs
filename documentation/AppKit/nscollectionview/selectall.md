# selectAll(_:)

**Framework**: AppKit  
**Kind**: method

Selects all items in the collection view, if doing so is possible.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@IBAction
@MainActor func selectAll(_ sender: Any?)
```

#### Discussion

This method works only when the [`isSelectable`](nscollectionview/isselectable.md) and [`allowsMultipleSelection`](nscollectionview/allowsmultipleselection.md) properties are both [`true`](https://developer.apple.com/documentation/Swift/true). If either property is set to [`false`](https://developer.apple.com/documentation/Swift/false), this method quietly does nothing and any connected menu item is disabled.

This method consults the delegate object regarding the selection. Specifically, it calls the delegate’s [`collectionView(_:shouldSelectItemsAt:)`](nscollectionviewdelegate/collectionview(_:shouldselectitemsat:).md) method to see if the items should be selected. For any items that are selected, it calls the [`collectionView(_:didSelectItemsAt:)`](nscollectionviewdelegate/collectionview(_:didselectitemsat:).md) method.

## Parameters

- `sender`: The object that requested the action. You may specify   for this property.

## See Also

- [var isSelectable: Bool](nscollectionview/isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](nscollectionview/allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](nscollectionview/allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [var selectionIndexPaths: Set<IndexPath>](nscollectionview/selectionindexpaths.md)
  The set of index paths representing the currently selected items.
- [func deselectAll(Any?)](nscollectionview/deselectall(_:).md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/selectitems(at:scrollposition:).md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](nscollectionview/deselectitems(at:).md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/selectall(_:))*