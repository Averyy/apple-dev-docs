# collectionView(_:willDisplaySupplementaryView:forElementKind:at:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified supplementary view is about to be displayed in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, willDisplaySupplementaryView view: UICollectionReusableView, forElementKind elementKind: String, at indexPath: IndexPath)
```

#### Discussion

The collection view calls this method before adding a supplementary view to its content. Use this method to detect view additions, as opposed to monitoring the view itself to see when it appears.

## Parameters

- `collectionView`: The collection view object that is adding the supplementary view.
- `view`: The view being added.
- `elementKind`: The type of the supplementary view. This string is defined by the layout that presents the view.
- `indexPath`: The index path of the data item that the supplementary view represents.

## See Also

- [func collectionView(UICollectionView, willDisplay: UICollectionViewCell, forItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:).md)
  Tells the delegate that the specified cell is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplaying: UICollectionViewCell, forItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didenddisplaying:foritemat:).md)
  Tells the delegate that the specified cell was removed from the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](uicollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:).md)
  Tells the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplaysupplementaryview:forelementkind:at:))*