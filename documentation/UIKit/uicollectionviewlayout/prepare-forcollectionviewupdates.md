# prepare(forCollectionViewUpdates:)

**Framework**: UIKit  
**Kind**: method

Notifies the layout object that the contents of the collection view are about to change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func prepare(forCollectionViewUpdates updateItems: [UICollectionViewUpdateItem])
```

#### Discussion

When items are inserted or deleted, the collection view notifies its layout object so that it can adjust the layout as needed. The first step in that process is to call this method to let the layout object know what changes to expect. After that, additional calls are made to gather layout information for inserted, deleted, and moved items that are going to be animated around the collection view.

## Parameters

- `updateItems`: An array of   objects that identify the changes being made.

## See Also

- [func finalizeCollectionViewUpdates()](uicollectionviewlayout/finalizecollectionviewupdates.md)
  Performs any additional animations or clean up needed during a collection view update.
- [func indexPathsToInsertForSupplementaryView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:).md)
  Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [func indexPathsToInsertForDecorationView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertfordecorationview(ofkind:).md)
  Retrieves an array of index paths representing the decoration views to add.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
  Retrieves the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
  Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
  Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:).md)
  Retrieves an array of index paths representing the supplementary views to remove.
- [func indexPathsToDeleteForDecorationView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstodeletefordecorationview(ofkind:).md)
  Retrieves an array of index paths representing the decoration views to remove.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
  Retrieves the final layout information for an item that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
  Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
  Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [func targetIndexPath(forInteractivelyMovingItem: IndexPath, withPosition: CGPoint) -> IndexPath](uicollectionviewlayout/targetindexpath(forinteractivelymovingitem:withposition:).md)
  Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/prepare(forcollectionviewupdates:))*