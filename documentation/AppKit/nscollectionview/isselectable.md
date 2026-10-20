# isSelectable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user may select items in the collection view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isSelectable: Bool { get set }
```

```objc
@property (getter=isSelectable) BOOL selectable;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the collection view allows the user to select items, or [`false`](../../Swift/false.md) when it does not. You can set selections programmatically regardless of this setting.

The default value of this property is [`false`](../../Swift/false.md). Changing the value from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md) removes the current selection if there is one.

## See Also

### Managing the Selection
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/isselectable)*