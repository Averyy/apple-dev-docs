# deselectItem(at:animated:)

**Framework**: UIKit  
**Kind**: method

Deselects the item at the specified index.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func deselectItem(at indexPath: IndexPath, animated: Bool)
```

#### Discussion

If the [`allowsSelection`](uicollectionview/allowsselection.md) property is [`false`](https://developer.apple.com/documentation/swift/false), calling this method has no effect.

This method doesn’t cause any selection-related delegate methods to be called.

## Parameters

- `indexPath`: The index path of the item to select. Specifying   results in no change to the current selection.
- `animated`: Specify   to animate the change in the selection or   to make the change without animating it.

## See Also

- [var indexPathsForSelectedItems: [IndexPath]?](uicollectionview/indexpathsforselecteditems.md)
  The index paths for the selected items.
- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](uicollectionview/selectitem(at:animated:scrollposition:).md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [var allowsSelection: Bool](uicollectionview/allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [var allowsMultipleSelection: Bool](uicollectionview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one item in the collection view.
- [var allowsSelectionDuringEditing: Bool](uicollectionview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uicollectionview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/deselectitem(at:animated:))*