# selectionIndexPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of index paths representing the currently selected items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var selectionIndexPaths: Set<IndexPath> { get set }
```

```objc
@property (copy) NSSet<NSIndexPath *> * selectionIndexPaths;
```

#### Discussion

This property reflects the index paths of the currently selected items, where each index path contains a [`section`](../../Foundation/nsindexpath/section.md) number and an index number for the [`item`](../../Foundation/nsindexpath/item.md) in that section. This property is updated automatically when the user selects items interactively. You can also change the selection programmatically by assigning a new value to this property. To animate changes to the selection, call this method on the collection view’s [`animator()`](../nsanimatablepropertycontainer/animator%28%29.md) proxy object instead.

It is a programmer error to specify an index path that does not refer to a valid item in the data source. If you specify an invalid index path, this method raises an exception.

This property is key-value observable. Other methods that modify the selection automatically update this property.

## See Also

### Managing the Selection
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that indicates whether the user may select items in the collection view.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that indicates whether the user may select more than one item in the collection view.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the collection view may have no selected items.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all items in the collection view, if doing so is possible.
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all items in the collection view.
- [func selectItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./selectitems%28at,scrollposition%29.md)
  Adds the specified items to the current selection and optionally scrolls the items into position.
- [func deselectItems(at: Set<IndexPath>)](./deselectitems%28at%29.md)
  Removes the specified items from the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/selectionindexpaths)*