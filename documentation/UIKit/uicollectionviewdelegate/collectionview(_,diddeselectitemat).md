# collectionView(_:didDeselectItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the item at the specified path was deselected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, didDeselectItemAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView didDeselectItemAtIndexPath:(NSIndexPath *) indexPath;
```

#### Discussion

The collection view calls this method when the user successfully deselects an item in the collection view. It does not call this method when you programmatically deselect items.

## Parameters

- `collectionView`: The collection view object that is notifying you of the selection change.
- `indexPath`: The index path of the cell that was deselected.

## See Also

### Managing the selected cells
- [Changing the appearance of selected and highlighted cells](../changing-the-appearance-of-selected-and-highlighted-cells.md)
  Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func collectionView(UICollectionView, shouldSelectItemAt: IndexPath) -> Bool](./collectionview%28_,shouldselectitemat%29.md)
  Asks the delegate if the specified item should be selected.
- [func collectionView(UICollectionView, didSelectItemAt: IndexPath)](./collectionview%28_,didselectitemat%29.md)
  Tells the delegate that the item at the specified index path was selected.
- [func collectionView(UICollectionView, shouldDeselectItemAt: IndexPath) -> Bool](./collectionview%28_,shoulddeselectitemat%29.md)
  Asks the delegate if the specified item should be deselected.
- [func collectionView(UICollectionView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](./collectionview%28_,shouldbeginmultipleselectioninteractionat%29.md)
  Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [func collectionView(UICollectionView, didBeginMultipleSelectionInteractionAt: IndexPath)](./collectionview%28_,didbeginmultipleselectioninteractionat%29.md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [func collectionViewDidEndMultipleSelectionInteraction(UICollectionView)](./collectionviewdidendmultipleselectioninteraction%28_%29.md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:diddeselectitemat:))*