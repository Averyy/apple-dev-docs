# indexPathsToDeleteForSupplementaryView(ofKind:)

**Framework**: UIKit  
**Kind**: method

Retrieves an array of index paths representing the supplementary views to remove.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func indexPathsToDeleteForSupplementaryView(ofKind elementKind: String) -> [IndexPath]
```

#### Return Value

An array of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects indicating the supplementary views you want to remove or an empty array if you do not want to remove any views of the given kind.

#### Discussion

The collection view calls this method whenever you delete cells or sections to the collection view. Implementing this method gives your layout object an opportunity to remove any supplementary views that are no longer needed.

The collection view calls this method between its calls to [`prepare(forCollectionViewUpdates:)`](uicollectionviewlayout/prepare(forcollectionviewupdates:).md) and [`finalizeCollectionViewUpdates()`](uicollectionviewlayout/finalizecollectionviewupdates().md).

## Parameters

- `elementKind`: The specific type of supplementary view.

## See Also

- [func prepare(forCollectionViewUpdates: [UICollectionViewUpdateItem])](uicollectionviewlayout/prepare(forcollectionviewupdates:).md)
  Notifies the layout object that the contents of the collection view are about to change.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:))*