# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the user may select more than one item in the collection view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the collection view supports the selection of more than one item at a time. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). Changing the value from [`true`](https://developer.apple.com/documentation/Swift/true) to [`false`](https://developer.apple.com/documentation/Swift/false) reduces the current selection to the first item in the selected group.

## See Also

- [var isSelectable: Bool](nscollectionview/isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsEmptySelection: Bool](nscollectionview/allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [var selectionIndexPaths: Set<IndexPath>](nscollectionview/selectionindexpaths.md)
  The set of index paths representing the currently selected items.
- [func selectAll(Any?)](nscollectionview/selectall(_:).md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](nscollectionview/deselectall(_:).md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/selectitems(at:scrollposition:).md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](nscollectionview/deselectitems(at:).md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/allowsmultipleselection)*