# allowsEmptySelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the collection view may have no selected items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var allowsEmptySelection: Bool { get set }
```

```objc
@property BOOL allowsEmptySelection;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which allows the collection view to have no selected items. Setting this property to [`false`](../../Swift/false.md) causes the collection view to always leave at least one item selected.

## See Also

### Managing the Selection
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var selectionIndexPaths: Set<IndexPath>](./selectionindexpaths.md)
  The set of index paths representing the currently selected items.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./selectitems%28at,scrollposition%29.md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](./deselectitems%28at%29.md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/allowsemptyselection)*