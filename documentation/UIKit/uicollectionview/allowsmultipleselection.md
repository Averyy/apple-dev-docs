# allowsMultipleSelection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether users can select more than one item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsMultipleSelection;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

#### Discussion

This property controls whether multiple items can be selected simultaneously. The default value of this property is [`false`](../../Swift/false.md).

When the value of this property is [`true`](../../Swift/true.md), tapping a cell adds it to the current selection (assuming the delegate permits the cell to be selected). Tapping the cell again removes it from the selection.

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
- [var allowsSelectionDuringEditing: Bool](./allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](./allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/allowsmultipleselection)*