# indexPathsForSelectedItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index paths for the selected items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indexPathsForSelectedItems: [IndexPath]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSIndexPath *> * indexPathsForSelectedItems;
```

## Discussion

The value of this property is an array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects, each of which corresponds to a single selected item. If there are no selected items, the value of this property is `nil`.

## See Also

### Selecting cells
- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](./selectitem%28at,animated,scrollposition%29.md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [func deselectItem(at: IndexPath, animated: Bool)](./deselectitem%28at,animated%29.md)
  Deselects the item at the specified index.
- [var allowsSelection: Bool](./allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one item in the collection view.
- [var allowsSelectionDuringEditing: Bool](./allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](./allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforselecteditems)*