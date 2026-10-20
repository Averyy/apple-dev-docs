# initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the starting layout information for a decoration view being added to the collection view.

**Availability**:
- macOS

## Declaration

```swift
func initialLayoutAttributesForAppearingDecorationElement(ofKind elementKind: NSCollectionView.DecorationElementKind, at decorationIndexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

```objc
- (NSCollectionViewLayoutAttributes *) initialLayoutAttributesForAppearingDecorationElementOfKind:(NSCollectionViewDecorationElementKind) elementKind atIndexPath:(NSIndexPath *) decorationIndexPath;
```

#### Return Value

The layout attributes object that describes the decoration view’s position and properties at the start of animations.

#### Discussion

When your layout object adds decoration views in response to other changes in the collection view, the collection view calls this method for each decoration view before animating it onscreen. Because new decoration views are not yet visible in the collection view, the attributes you return represent the view’s starting state. For example, you might return attributes that position the decoration view offscreen or set its initial alpha to `0`. The collection view uses the attributes you return as the starting point for any animations. (The end point of the animation is the view’s new location and attributes.) If you return `nil`, the layout uses the decoration view’s final attributes for both the start point and end point of the animation.

The default implementation of this method returns `nil`. Subclasses are expected to override this method, as needed, and provide any initial attributes.

## Parameters

- `elementKind`: The type of the decoration view being added.
- `decorationIndexPath`: The index path of the decoration view. You can use this path to retrieve any relevant information from the collection view’s data source.

## See Also

### Responding to Collection View Updates
- [func prepare(forCollectionViewUpdates: [NSCollectionViewUpdateItem])](./prepare%28forcollectionviewupdates%29.md)
  Performs needed tasks before items are inserted, deleted, or moved within the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:))*