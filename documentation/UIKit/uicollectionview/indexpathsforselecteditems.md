# indexPathsForSelectedItems

**Framework**: UIKit  
**Kind**: property

The index paths for the selected items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indexPathsForSelectedItems: [IndexPath]? { get }
```

#### Discussion

The value of this property is an array of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects, each of which corresponds to a single selected item. If there are no selected items, the value of this property is `nil`.

## See Also

- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](uicollectionview/selectitem(at:animated:scrollposition:).md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [func deselectItem(at: IndexPath, animated: Bool)](uicollectionview/deselectitem(at:animated:).md)
  Deselects the item at the specified index.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforselecteditems)*