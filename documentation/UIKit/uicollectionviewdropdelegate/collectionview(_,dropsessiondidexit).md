# collectionView(_:dropSessionDidExit:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies you when dragged content exits the collection view’s bounds rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidExit session: any UIDropSession)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView dropSessionDidExit:(id<UIDropSession>) session;
```

## Discussion

UIKit calls this method when dragged content exits the bounds rectangle of the specified collection view. The method isn’t called again until the dragged content enters the collection view’s bounds (triggering a call to the [`collectionView(_:dropSessionDidEnter:)`](./collectionview%28_,dropsessiondidenter%29.md) method) and exits again.

Use this method to clean up any state information that you configured in your [`collectionView(_:dropSessionDidEnter:)`](./collectionview%28_,dropsessiondidenter%29.md) method.

## Parameters

- `collectionView`: The collection view that was tracking the dragged content.
- `session`: The drop session object containing information about the type of data being dragged.

## See Also

### Tracking the drag movements
- [func collectionView(UICollectionView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UICollectionViewDropProposal](./collectionview%28_,dropsessiondidupdate,withdestinationindexpath%29.md)
  Tells your delegate that the position of the dragged data over the collection view changed.
- [func collectionView(UICollectionView, dropSessionDidEnter: any UIDropSession)](./collectionview%28_,dropsessiondidenter%29.md)
  Notifies you when dragged content enters the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidEnd: any UIDropSession)](./collectionview%28_,dropsessiondidend%29.md)
  Notifies you when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidexit:))*