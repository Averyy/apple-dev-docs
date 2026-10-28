# visibleSupplementaryViews(ofKind:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets an array of the visible supplementary views of the specified kind.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func visibleSupplementaryViews(ofKind elementKind: String) -> [UICollectionReusableView]
```

```objc
- (NSArray<UICollectionReusableView *> *) visibleSupplementaryViewsOfKind:(NSString *) elementKind;
```

## Return Value

An array of the visible supplementary views. If no supplementary views are visible, the returned array is empty.

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
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](./indexpathsforvisiblesupplementaryelements%28ofkind%29.md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](./supplementaryview%28forelementkind,at%29.md)
  Gets the supplementary view at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/visiblesupplementaryviews(ofkind:))*