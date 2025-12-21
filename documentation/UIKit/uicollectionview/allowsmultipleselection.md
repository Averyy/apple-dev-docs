# allowsMultipleSelection

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether users can select more than one item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

This property controls whether multiple items can be selected simultaneously. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), tapping a cell adds it to the current selection (assuming the delegate permits the cell to be selected). Tapping the cell again removes it from the selection.

## See Also

- [var indexPathsForSelectedItems: [IndexPath]?](uicollectionview/indexpathsforselecteditems.md)
  The index paths for the selected items.
- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](uicollectionview/selectitem(at:animated:scrollposition:).md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [func deselectItem(at: IndexPath, animated: Bool)](uicollectionview/deselectitem(at:animated:).md)
  Deselects the item at the specified index.
- [var allowsSelection: Bool](uicollectionview/allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [var allowsSelectionDuringEditing: Bool](uicollectionview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uicollectionview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/allowsmultipleselection)*