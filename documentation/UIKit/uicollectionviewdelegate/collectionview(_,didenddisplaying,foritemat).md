# collectionView(_:didEndDisplaying:forItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified cell was removed from the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, didEndDisplaying cell: UICollectionViewCell, forItemAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView didEndDisplayingCell:(UICollectionViewCell *) cell forItemAtIndexPath:(NSIndexPath *) indexPath;
```

#### Discussion

Use this method to detect when a cell is removed from a collection view, as opposed to monitoring the view itself to see when it disappears.

## Parameters

- `collectionView`: The collection view object that removed the cell.
- `cell`: The cell object that was removed.
- `indexPath`: The index path of the data item that the cell represented.

## See Also

### Tracking the addition and removal of views
- [func collectionView(UICollectionView, willDisplay: UICollectionViewCell, forItemAt: IndexPath)](./collectionview%28_,willdisplay,foritemat%29.md)
  Tells the delegate that the specified cell is about to be displayed in the collection view.
- [func collectionView(UICollectionView, willDisplaySupplementaryView: UICollectionReusableView, forElementKind: String, at: IndexPath)](./collectionview%28_,willdisplaysupplementaryview,forelementkind,at%29.md)
  Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](./collectionview%28_,didenddisplayingsupplementaryview,forelementofkind,at%29.md)
  Tells the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didenddisplaying:foritemat:))*