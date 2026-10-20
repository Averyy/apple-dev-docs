# prepare(forCollectionViewUpdates:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs needed tasks before items are inserted, deleted, or moved within the collection view.

**Availability**:
- macOS

## Declaration

```swift
func prepare(forCollectionViewUpdates updateItems: [NSCollectionViewUpdateItem])
```

```objc
- (void) prepareForCollectionViewUpdates:(NSArray<NSCollectionViewUpdateItem *> *) updateItems;
```

#### Discussion

When items are inserted, deleted, or moved, the collection view calls this method to report those changes to the layout object. The default implementation uses the provided information to plan the layout animations needed to respond to the changes. Subclasses can override this method and use it to prepare for any custom changes, but you should always call `super` at some point in your implementation.

## Parameters

- `updateItems`: An array of [`NSCollectionViewUpdateItem`](../nscollectionviewupdateitem.md) objects that identify the changes being made.

## See Also

### Responding to Collection View Updates
- [func finalizeCollectionViewUpdates()](./finalizecollectionviewupdates%28%29.md)
  Performs needed steps after items are inserted, deleted, or moved within a collection view.
- [func indexPathsToInsertForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](./indexpathstoinsertforsupplementaryview%28ofkind%29.md)
  Returns the index paths for any supplementary views that the layout object wants to add to the collection view.
- [func indexPathsToInsertForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](./indexpathstoinsertfordecorationview%28ofkind%29.md)
  Returns the index paths for any decoration views that the layout object wants to add to the collection view.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](./initiallayoutattributesforappearingitem%28at%29.md)
  Returns the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./initiallayoutattributesforappearingsupplementaryelement%28ofkind,at%29.md)
  Returns the starting layout information for a supplementary view being added to the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./initiallayoutattributesforappearingdecorationelement%28ofkind,at%29.md)
  Returns the starting layout information for a decoration view being added to the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](./indexpathstodeleteforsupplementaryview%28ofkind%29.md)
  Returns the index paths for any supplementary views that the layout object wants to remove from the collection view.
- [func indexPathsToDeleteForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](./indexpathstodeletefordecorationview%28ofkind%29.md)
  Returns index paths for any decoration views that the layout object wants to remove from the collection view.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingitem%28at%29.md)
  Returns the ending layout information for an item being removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingsupplementaryelement%28ofkind,at%29.md)
  Returns the ending layout information for a supplementary view being removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingdecorationelement%28ofkind,at%29.md)
  Returns the ending layout information for a decoration view being removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/prepare(forcollectionviewupdates:))*