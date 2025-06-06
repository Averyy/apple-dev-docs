# initialLayoutAttributesForAppearingSupplementaryElement(ofKind:at:)

**Framework**: AppKit  
**Kind**: method

Returns the starting layout information for a supplementary view being added to the collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func initialLayoutAttributesForAppearingSupplementaryElement(ofKind elementKind: NSCollectionView.SupplementaryElementKind, at elementIndexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

#### Return Value

The layout attributes object that describes the supplementary view’s position and properties at the start of animations.

#### Discussion

When your layout object adds supplementary views in response to other changes in the collection view, the collection view calls this method for each supplementary view before animating it onscreen. Because new supplementary views are not yet visible in the collection view, the attributes you return represent the view’s starting state. For example, you might return attributes that position the supplementary view offscreen or set its initial alpha to `0`. The collection view uses the attributes you return as the starting point for any animations. (The end point of the animation is the view’s new location and attributes.) If you return `nil`, the layout uses the supplementary view’s final attributes for both the start point and end point of the animation.

The default implementation of this method returns `nil`. Subclasses are expected to override this method, as needed, and provide any initial attributes.

## Parameters

- `elementKind`: The type of the supplementary view being added.
- `elementIndexPath`: The index path of the supplementary view. You can use this path to retrieve any relevant information from the collection view’s data source.

## See Also

- [func prepare(forCollectionViewUpdates: [NSCollectionViewUpdateItem])](nscollectionviewlayout/prepare(forcollectionviewupdates:).md)
  Performs needed tasks before items are inserted, deleted, or moved within the collection view.
- [func finalizeCollectionViewUpdates()](nscollectionviewlayout/finalizecollectionviewupdates.md)
  Performs needed steps after items are inserted, deleted, or moved within a collection view.
- [func indexPathsToInsertForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:).md)
  Returns the index paths for any supplementary views that the layout object wants to add to the collection view.
- [func indexPathsToInsertForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstoinsertfordecorationview(ofkind:).md)
  Returns the index paths for any decoration views that the layout object wants to add to the collection view.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
  Returns the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
  Returns the starting layout information for a decoration view being added to the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:).md)
  Returns the index paths for any supplementary views that the layout object wants to remove from the collection view.
- [func indexPathsToDeleteForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstodeletefordecorationview(ofkind:).md)
  Returns index paths for any decoration views that the layout object wants to remove from the collection view.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
  Returns the ending layout information for an item being removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
  Returns the ending layout information for a supplementary view being removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
  Returns the ending layout information for a decoration view being removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:))*