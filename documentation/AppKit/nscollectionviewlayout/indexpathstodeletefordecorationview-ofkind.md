# indexPathsToDeleteForDecorationView(ofKind:)

**Framework**: AppKit  
**Kind**: method

Returns index paths for any decoration views that the layout object wants to remove from the collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexPathsToDeleteForDecorationView(ofKind elementKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>
```

#### Return Value

The set of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects representing the decoration views to remove, or an empty array if you do not want to remove any decoration views.

#### Discussion

When your app inserts or deletes items or sections in the collection view, the collection view calls this method for each of the registered decoration view types. The default implementation returns an empty array, but you can override it and return index paths for each decoration view you want to remove. For example, when a section is removed, you might want to remove the decoration views associated with that section. In that case, you would add index paths to the array that contain the section numbers that were removed.

The index paths you return should always contain a valid section number, but the item number is optional. The item number is necessary only if you support multiple supplementary views of the same type in a single section. If you do, your layout object can use the item numbers internally to differentiate the supplementary views.

Subclasses are expected to override this method, as needed, and provide any appropriate index paths.

## Parameters

- `elementKind`: The type of the decoration views to remove.

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
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
  Returns the starting layout information for a supplementary view being added to the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
  Returns the starting layout information for a decoration view being added to the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:).md)
  Returns the index paths for any supplementary views that the layout object wants to remove from the collection view.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
  Returns the ending layout information for an item being removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
  Returns the ending layout information for a supplementary view being removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
  Returns the ending layout information for a decoration view being removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/indexpathstodeletefordecorationview(ofkind:))*