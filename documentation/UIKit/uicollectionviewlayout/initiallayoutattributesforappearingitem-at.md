# initialLayoutAttributesForAppearingItem(at:)

**Framework**: UIKit  
**Kind**: method

Retrieves the starting layout information for an item being inserted into the collection view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func initialLayoutAttributesForAppearingItem(at itemIndexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

A layout attributes object that describes the position at which to place the corresponding cell.

#### Discussion

This method is called after the [`prepare(forCollectionViewUpdates:)`](uicollectionviewlayout/prepare(forcollectionviewupdates:).md) method and before the [`finalizeCollectionViewUpdates()`](uicollectionviewlayout/finalizecollectionviewupdates().md) method for any items that are about to be inserted. Your implementation should return the layout information that describes the initial position and state of the item. The collection view uses this information as the starting point for any animations. (The end point of the animation is the item’s new location in the collection view.) If you return `nil`, the layout object uses the item’s final attributes for both the start and end points of the animation.

The default implementation of this method returns `nil`.

## Parameters

- `itemIndexPath`: The index path of the item being inserted. You can use this path to locate the item in the collection view’s data source.

## See Also

- [func prepare(forCollectionViewUpdates: [UICollectionViewUpdateItem])](uicollectionviewlayout/prepare(forcollectionviewupdates:).md)
  Notifies the layout object that the contents of the collection view are about to change.
- [func finalizeCollectionViewUpdates()](uicollectionviewlayout/finalizecollectionviewupdates.md)
  Performs any additional animations or clean up needed during a collection view update.
- [func indexPathsToInsertForSupplementaryView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:).md)
  Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [func indexPathsToInsertForDecorationView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertfordecorationview(ofkind:).md)
  Retrieves an array of index paths representing the decoration views to add.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/initiallayoutattributesforappearingitem(at:))*