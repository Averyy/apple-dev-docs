# indexPathsToInsertForSupplementaryView(ofKind:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves an array of index paths for the supplementary views you want to add to the layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func indexPathsToInsertForSupplementaryView(ofKind elementKind: String) -> [IndexPath]
```

```objc
- (NSArray<NSIndexPath *> *) indexPathsToInsertForSupplementaryViewOfKind:(NSString *) elementKind;
```

## Return Value

An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects indicating the location of the new supplementary views, or an empty array if you don’t want to add any supplementary views.

## Discussion

The collection view calls this method whenever you add cells or sections to the collection view. Implementing this method gives your layout object an opportunity to add new supplementary views to complement the additions.

The collection view calls this method between its calls to [`prepare(forCollectionViewUpdates:)`](./prepare%28forcollectionviewupdates%29.md) and [`finalizeCollectionViewUpdates()`](./finalizecollectionviewupdates%28%29.md).

## Parameters

- `elementKind`: The specific type of supplementary view.

## See Also

### Responding to collection view updates
- [func prepare(forCollectionViewUpdates: [UICollectionViewUpdateItem])](./prepare%28forcollectionviewupdates%29.md)
  Notifies the layout object that the contents of the collection view are about to change.
- [func finalizeCollectionViewUpdates()](./finalizecollectionviewupdates%28%29.md)
  Performs any additional animations or clean up needed during a collection view update.
- [func indexPathsToInsertForDecorationView(ofKind: String) -> [IndexPath]](./indexpathstoinsertfordecorationview%28ofkind%29.md)
  Retrieves an array of index paths representing the decoration views to add.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](./initiallayoutattributesforappearingitem%28at%29.md)
  Retrieves the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./initiallayoutattributesforappearingsupplementaryelement%28ofkind,at%29.md)
  Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./initiallayoutattributesforappearingdecorationelement%28ofkind,at%29.md)
  Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: String) -> [IndexPath]](./indexpathstodeleteforsupplementaryview%28ofkind%29.md)
  Retrieves an array of index paths representing the supplementary views to remove.
- [func indexPathsToDeleteForDecorationView(ofKind: String) -> [IndexPath]](./indexpathstodeletefordecorationview%28ofkind%29.md)
  Retrieves an array of index paths representing the decoration views to remove.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingitem%28at%29.md)
  Retrieves the final layout information for an item that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingsupplementaryelement%28ofkind,at%29.md)
  Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./finallayoutattributesfordisappearingdecorationelement%28ofkind,at%29.md)
  Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [func targetIndexPath(forInteractivelyMovingItem: IndexPath, withPosition: CGPoint) -> IndexPath](./targetindexpath%28forinteractivelymovingitem,withposition%29.md)
  Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:))*