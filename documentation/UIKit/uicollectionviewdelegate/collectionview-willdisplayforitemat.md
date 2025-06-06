# collectionView(_:willDisplay:forItemAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified cell is about to be displayed in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt indexPath: IndexPath)
```

#### Discussion

The collection view calls this method before adding a cell to its content. Use this method to detect cell additions, as opposed to monitoring the cell itself to see when it appears.

## Parameters

- `collectionView`: The collection view object that is adding the cell.
- `cell`: The cell object being added.
- `indexPath`: The index path of the data item that the cell represents.

## See Also

- [func collectionView(UICollectionView, willDisplaySupplementaryView: UICollectionReusableView, forElementKind: String, at: IndexPath)](uicollectionviewdelegate/collectionview(_:willdisplaysupplementaryview:forelementkind:at:).md)
  Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplaying: UICollectionViewCell, forItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didenddisplaying:foritemat:).md)
  Tells the delegate that the specified cell was removed from the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](uicollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:).md)
  Tells the delegate that the specified supplementary view was removed from the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:))*