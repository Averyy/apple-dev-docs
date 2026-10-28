# finalizeCollectionViewUpdates()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs needed steps after items are inserted, deleted, or moved within a collection view.

**Availability**:
- macOS

## Declaration

```swift
func finalizeCollectionViewUpdates()
```

```objc
- (void) finalizeCollectionViewUpdates;
```

## Discussion

When items are inserted, deleted, or moved, the collection view calls this method as a final step before performing the associated animations. This method is called within the animation block used to configure the insertion, deletion, and move animations, so you can use this method to configure additional animations that you want to run at the same time. You can also use this method to perform any cleanup steps to account for the changes.

## See Also

### Responding to Collection View Updates
- [func prepare(forCollectionViewUpdates: [NSCollectionViewUpdateItem])](./prepare%28forcollectionviewupdates%29.md)
  Performs needed tasks before items are inserted, deleted, or moved within the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/finalizecollectionviewupdates())*