# collectionView(_:willDisplaySupplementaryView:forElementKind:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified supplementary view is about to be displayed in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, at indexPath: IndexPath)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView willDisplaySupplementaryView:(UICollectionReusableView *) view forElementKind:(NSString *) elementKind atIndexPath:(NSIndexPath *) indexPath;
```

## Discussion

The collection view calls this method before adding a supplementary view to its content. Use this method to detect view additions, as opposed to monitoring the view itself to see when it appears.

## Parameters

- `collectionView`: The collection view object that is adding the supplementary view.
- `view`: The view being added.
- `elementKind`: The type of the supplementary view. This string is defined by the layout that presents the view.
- `indexPath`: The index path of the data item that the supplementary view represents.

## See Also

### Tracking the addition and removal of views
- [func collectionView(UICollectionView, willDisplay: UICollectionViewCell, forItemAt: IndexPath)](./collectionview%28_,willdisplay,foritemat%29.md)
  Tells the delegate that the specified cell is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplaying: UICollectionViewCell, forItemAt: IndexPath)](./collectionview%28_,didenddisplaying,foritemat%29.md)
  Tells the delegate that the specified cell was removed from the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](./collectionview%28_,didenddisplayingsupplementaryview,forelementofkind,at%29.md)
  Tells the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplaysupplementaryview:forelementkind:at:))*