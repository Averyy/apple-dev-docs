# deselectAll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deselects all items in the collection view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@IBAction
func deselectAll(_ sender: Any?)
```

```objc
- (void) deselectAll:(id) sender;
```

## Discussion

This method works only when the [`isSelectable`](./isselectable.md) and [`allowsEmptySelection`](./allowsemptyselection.md) properties are both true  [`true`](../../Swift/true.md). If either property is set to [`false`](../../Swift/false.md), this method quietly does nothing and any connected menu item is disabled.

This method consults the delegate object regarding the selection. Specifically, it calls the delegate’s [`collectionView(_:shouldDeselectItemsAt:)`](../nscollectionviewdelegate/collectionview%28_,shoulddeselectitemsat%29.md) method to see if the items should be selected. For any items that are selected, it calls the [`collectionView(_:didDeselectItemsAt:)`](../nscollectionviewdelegate/collectionview%28_,diddeselectitemsat%29.md) method.

## Parameters

- `sender`: The object that requested the action. You may specify `nil` for this property.

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
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./selectitems%28at,scrollposition%29.md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](./deselectitems%28at%29.md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/deselectall(_:))*