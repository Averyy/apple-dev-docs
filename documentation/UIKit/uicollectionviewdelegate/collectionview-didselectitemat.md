# collectionView(_:didSelectItemAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the item at the specified index path was selected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath)
```

#### Discussion

The collection view calls this method when the user successfully selects an item in the collection view. It does not call this method when you programmatically set the selection.

## Parameters

- `collectionView`: The collection view object that is notifying you of the selection change.
- `indexPath`: The index path of the cell that was selected.

## See Also

- [Changing the appearance of selected and highlighted cells](changing-the-appearance-of-selected-and-highlighted-cells.md)
  Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func collectionView(UICollectionView, shouldSelectItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md)
  Asks the delegate if the specified item should be selected.
- [func collectionView(UICollectionView, shouldDeselectItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shoulddeselectitemat:).md)
  Asks the delegate if the specified item should be deselected.
- [func collectionView(UICollectionView, didDeselectItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:diddeselectitemat:).md)
  Tells the delegate that the item at the specified path was deselected.
- [func collectionView(UICollectionView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldbeginmultipleselectioninteractionat:).md)
  Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [func collectionView(UICollectionView, didBeginMultipleSelectionInteractionAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [func collectionViewDidEndMultipleSelectionInteraction(UICollectionView)](uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didselectitemat:))*