# targetIndexPath(forInteractivelyMovingItem:withPosition:)

**Framework**: UIKit  
**Kind**: method

Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func targetIndexPath(forInteractivelyMovingItem previousIndexPath: IndexPath, withPosition position: CGPoint) -> IndexPath
```

#### Return Value

The index path corresponding to the specified location in the collection view.

#### Discussion

During interactive movement of an item, this method maps points in the collection view’s bounds rectangle to index paths that correspond to the locations of those points. The default implementation of this method searches for an existing cell at the specified location and returns the index path of that cell. If there are multiple cells at the same location, the method returns the topmost cell—that is, the cell whose [`zIndex`](uicollectionviewlayoutattributes/zindex.md) layout attribute value is greatest.

You can override this method as needed to change how the index path is determined. For example, you might return the index path of the cell that has the lowest [`zIndex`](uicollectionviewlayoutattributes/zindex.md) value instead of the highest. If you override this method, you do not need to call `super`.

## Parameters

- `previousIndexPath`: The previous index path of the item. Use this value to identify the item.
- `position`: The target point in the collection view’s bounds. Use this value to compute the new index path for the item.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/targetindexpath(forinteractivelymovingitem:withposition:))*