# allowsSelectionDuringEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether users can select cells while the collection view is in editing mode.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var allowsSelectionDuringEditing: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsSelectionDuringEditing;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Selecting cells
- [var indexPathsForSelectedItems: [IndexPath]?](./indexpathsforselecteditems.md)
  The index paths for the selected items.
- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](./selectitem%28at,animated,scrollposition%29.md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [func deselectItem(at: IndexPath, animated: Bool)](./deselectitem%28at,animated%29.md)
  Deselects the item at the specified index.
- [var allowsSelection: Bool](./allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one item in the collection view.
- [var allowsMultipleSelectionDuringEditing: Bool](./allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/allowsselectionduringediting)*