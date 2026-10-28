# collectionView(_:willDisplay:forItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified cell is about to be displayed in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView willDisplayCell:(UICollectionViewCell *) cell forItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Discussion

The collection view calls this method before adding a cell to its content. Use this method to detect cell additions, as opposed to monitoring the cell itself to see when it appears.

## Parameters

- `collectionView`: The collection view object that is adding the cell.
- `cell`: The cell object being added.
- `indexPath`: The index path of the data item that the cell represents.

## See Also

### Tracking the addition and removal of views
- [func collectionView(UICollectionView, willDisplaySupplementaryView: UICollectionReusableView, forElementKind: String, at: IndexPath)](./collectionview%28_,willdisplaysupplementaryview,forelementkind,at%29.md)
  Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplaying: UICollectionViewCell, forItemAt: IndexPath)](./collectionview%28_,didenddisplaying,foritemat%29.md)
  Tells the delegate that the specified cell was removed from the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](./collectionview%28_,didenddisplayingsupplementaryview,forelementofkind,at%29.md)
  Tells the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:))*