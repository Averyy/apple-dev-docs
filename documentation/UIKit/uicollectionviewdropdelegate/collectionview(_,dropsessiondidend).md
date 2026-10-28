# collectionView(_:dropSessionDidEnd:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies you when the drag operation ends.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidEnd session: any UIDropSession)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView dropSessionDidEnd:(id<UIDropSession>) session;
```

## Discussion

The collection view calls this method at the conclusion of a drag that was over the collection view at one point. Use it to clean up any state information that you used to handle the drag. This method is called regardless of whether the data was actually dropped onto the collection view.

## Parameters

- `collectionView`: The collection view that’s tracking the dragged content.
- `session`: The drop session object containing information about the data being dragged.

## See Also

### Tracking the drag movements
- [func collectionView(UICollectionView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UICollectionViewDropProposal](./collectionview%28_,dropsessiondidupdate,withdestinationindexpath%29.md)
  Tells your delegate that the position of the dragged data over the collection view changed.
- [func collectionView(UICollectionView, dropSessionDidEnter: any UIDropSession)](./collectionview%28_,dropsessiondidenter%29.md)
  Notifies you when dragged content enters the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidExit: any UIDropSession)](./collectionview%28_,dropsessiondidexit%29.md)
  Notifies you when dragged content exits the collection view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidend:))*