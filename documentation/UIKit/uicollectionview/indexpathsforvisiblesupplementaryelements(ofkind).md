# indexPathsForVisibleSupplementaryElements(ofKind:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets the index paths of all visible supplementary views of the specified type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func indexPathsForVisibleSupplementaryElements(ofKind elementKind: String) -> [IndexPath]
```

```objc
- (NSArray<NSIndexPath *> *) indexPathsForVisibleSupplementaryElementsOfKind:(NSString *) elementKind;
```

## Return Value

An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects, each of which corresponds to a visible supplementary view in the collection view. If there are no visible supplementary views, this method returns an empty array.

## Parameters

- `elementKind`: The kind of supplementary view to locate. This value is defined by the layout object. This parameter must not be `nil`.

## See Also

### Locating items and views in the collection view
- [func indexPathForItem(at: CGPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](./indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](./indexpath%28for%29.md)
  Gets the index path of the specified cell.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](./cellforitem%28at%29.md)
  Gets the cell object at the index path you specify.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](./supplementaryview%28forelementkind,at%29.md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](./visiblesupplementaryviews%28ofkind%29.md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:))*