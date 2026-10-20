# collectionView(_:didBeginMultipleSelectionInteractionAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView didBeginMultipleSelectionInteractionAtIndexPath:(NSIndexPath *) indexPath;
```

#### Discussion

Your implementation of this method is a good place to indicate, in the app’s user interface, that the user is selecting multiple items; for example, you could replace an Edit or Select button with a Done button.

```swift
func collectionView(_ collectionView: UICollectionView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath) {
    // Replace the Select button with Done, and put the 
    // collection view into editing mode.
    setEditing(true, animated: true)
}
```

## Parameters

- `collectionView`: The collection view calling this method.
- `indexPath`: The index path of the item that the user touched to start the two-finger pan gesture.

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
- [func collectionView(UICollectionView, didDeselectItemAt: IndexPath)](./collectionview%28_,diddeselectitemat%29.md)
  Tells the delegate that the item at the specified path was deselected.
- [func collectionView(UICollectionView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](./collectionview%28_,shouldbeginmultipleselectioninteractionat%29.md)
  Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [func collectionViewDidEndMultipleSelectionInteraction(UICollectionView)](./collectionviewdidendmultipleselectioninteraction%28_%29.md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didbeginmultipleselectioninteractionat:))*