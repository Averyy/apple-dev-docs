# initialLayoutAttributesForAppearingSupplementaryElement(ofKind:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the starting layout information for a supplementary view being inserted into the collection view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func initialLayoutAttributesForAppearingSupplementaryElement(ofKind elementKind: String, at elementIndexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

```objc
- (UICollectionViewLayoutAttributes *) initialLayoutAttributesForAppearingSupplementaryElementOfKind:(NSString *) elementKind atIndexPath:(NSIndexPath *) elementIndexPath;
```

#### Return Value

A layout attributes object that describes the position at which to place the corresponding supplementary view.

#### Discussion

This method is called after the [`prepare(forCollectionViewUpdates:)`](./prepare%28forcollectionviewupdates%29.md) method and before the [`finalizeCollectionViewUpdates()`](./finalizecollectionviewupdates%28%29.md) method for any supplementary views that are about to be inserted. Your implementation should return the layout information that describes the initial position and state of the view. The collection view uses this information as the starting point for any animations. (The end point of the animation is the view’s new location in the collection view.) If you return `nil`, the layout object uses the item’s final attributes for both the start and end points of the animation.

The default implementation of this method returns `nil`.

## Parameters

- `elementKind`: A string that identifies the type of supplementary view.
- `elementIndexPath`: The index path of the item being inserted.

## See Also

### Responding to collection view updates
- [func prepare(forCollectionViewUpdates: [UICollectionViewUpdateItem])](./prepare%28forcollectionviewupdates%29.md)
  Notifies the layout object that the contents of the collection view are about to change.
- [func finalizeCollectionViewUpdates()](./finalizecollectionviewupdates%28%29.md)
  Performs any additional animations or clean up needed during a collection view update.
- [func indexPathsToInsertForSupplementaryView(ofKind: String) -> [IndexPath]](./indexpathstoinsertforsupplementaryview%28ofkind%29.md)
  Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [func indexPathsToInsertForDecorationView(ofKind: String) -> [IndexPath]](./indexpathstoinsertfordecorationview%28ofkind%29.md)
  Retrieves an array of index paths representing the decoration views to add.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](./initiallayoutattributesforappearingitem%28at%29.md)
  Retrieves the starting layout information for an item being inserted into the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:))*