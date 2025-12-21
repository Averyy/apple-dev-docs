# collectionView(_:shouldBeginMultipleSelectionInteractionAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, shouldBeginMultipleSelectionInteractionAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the user to select multiple items using a two-finger pan gesture; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) to disable the behavior. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When the system recognizes a two-finger pan gesture, it calls this method before it sets [`isEditing`](uicollectionview/isediting.md) to [`true`](https://developer.apple.com/documentation/Swift/true). If you return [`true`](https://developer.apple.com/documentation/Swift/true) from this method, the user can select multiple items using a two-finger pan gesture.

Users can select multiple items using the two-finger pan gesture on collection views that scroll either horizontally or vertically, but not both. Collection views that scroll in both directions won’t recognize the gesture or call this method.

If you don’t implement this method, the system uses the value of [`allowsMultipleSelectionDuringEditing`](uicollectionview/allowsmultipleselectionduringediting.md) to determine whether a user can select multiple items using a pan gesture.

## Parameters

- `collectionView`: The collection view calling this method.
- `indexPath`: The index path of the item that the user touched to start the two-finger pan gesture.

## See Also

- [Changing the appearance of selected and highlighted cells](changing-the-appearance-of-selected-and-highlighted-cells.md)
  Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func collectionView(UICollectionView, shouldSelectItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md)
  Asks the delegate if the specified item should be selected.
- [func collectionView(UICollectionView, didSelectItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didselectitemat:).md)
  Tells the delegate that the item at the specified index path was selected.
- [func collectionView(UICollectionView, shouldDeselectItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shoulddeselectitemat:).md)
  Asks the delegate if the specified item should be deselected.
- [func collectionView(UICollectionView, didDeselectItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:diddeselectitemat:).md)
  Tells the delegate that the item at the specified path was deselected.
- [func collectionView(UICollectionView, didBeginMultipleSelectionInteractionAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [func collectionViewDidEndMultipleSelectionInteraction(UICollectionView)](uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldbeginmultipleselectioninteractionat:))*