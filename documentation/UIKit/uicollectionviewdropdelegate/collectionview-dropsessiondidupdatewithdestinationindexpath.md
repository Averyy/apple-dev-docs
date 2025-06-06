# collectionView(_:dropSessionDidUpdate:withDestinationIndexPath:)

**Framework**: UIKit  
**Kind**: method

Tells your delegate that the position of the dragged data over the collection view changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidUpdate session: any UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UICollectionViewDropProposal
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Return Value

Your proposal for how to handle the content if it is dropped at the specified location.

#### Discussion

While the user is dragging content, the collection view calls this method repeatedly to determine how you would handle the drop if it occurred at the specified location. The collection view provides visual feedback to the user based on your proposal.

In your implementation of this method, create a [`UICollectionViewDropProposal`](uicollectionviewdropproposal.md) object and use it to convey your intentions. Because this method is called repeatedly while the user drags over the table view, your implementation should return as quickly as possible.

## Parameters

- `collectionView`: The collection view that’s tracking the dragged content.
- `session`: The drop session object containing information about the type of data being dragged.
- `destinationIndexPath`: The index path at which the content would be dropped.

## See Also

- [func collectionView(UICollectionView, dropSessionDidEnter: any UIDropSession)](uicollectionviewdropdelegate/collectionview(_:dropsessiondidenter:).md)
  Notifies you when dragged content enters the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidExit: any UIDropSession)](uicollectionviewdropdelegate/collectionview(_:dropsessiondidexit:).md)
  Notifies you when dragged content exits the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidEnd: any UIDropSession)](uicollectionviewdropdelegate/collectionview(_:dropsessiondidend:).md)
  Notifies you when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidupdate:withdestinationindexpath:))*