# collectionView(_:didUnhighlightItemAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the highlight was removed from the item at the specified index path.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAt indexPath: IndexPath)
```

#### Discussion

The collection view calls this method only in response to user interactions and does not call it if you programmatically change the highlighting on a cell.

## Parameters

- `collectionView`: The collection view object that is notifying you of the highlight change.
- `indexPath`: The index path of the cell that had its highlight removed.

## See Also

- [func collectionView(UICollectionView, shouldHighlightItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldhighlightitemat:).md)
  Asks the delegate if the item should be highlighted during tracking.
- [func collectionView(UICollectionView, didHighlightItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didhighlightitemat:).md)
  Tells the delegate that the item at the specified index path was highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didunhighlightitemat:))*