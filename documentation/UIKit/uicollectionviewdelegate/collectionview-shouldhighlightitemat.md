# collectionView(_:shouldHighlightItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the item should be highlighted during tracking.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the item should be highlighted or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

As touch events arrive, the collection view highlights items in anticipation of the user selecting them. As it processes those touch events, the collection view calls this method to ask your delegate if a given cell should be highlighted. It calls this method only in response to user interactions and does not call it if you programmatically set the highlighting on a cell.

If you return [`false`](https://developer.apple.com/documentation/swift/false) in your implementation, the cell does not get highlighted and the system bypasses the entire selection process. That is, the system does not call [`collectionView(_:shouldSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md) or any other selection-related methods. If you return [`true`](https://developer.apple.com/documentation/swift/true), [`isHighlighted`](uicollectionviewcell/ishighlighted.md) is set to [`true`](https://developer.apple.com/documentation/swift/true), [`collectionView(_:didHighlightItemAt:)`](uicollectionviewdelegate/collectionview(_:didhighlightitemat:).md) is called, and the system begins the selection process.

If you do not implement this method, the default return value is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `collectionView`: The collection view object that is asking about the highlight change.
- `indexPath`: The index path of the cell to be highlighted.

## See Also

- [func collectionView(UICollectionView, didHighlightItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didhighlightitemat:).md)
  Tells the delegate that the item at the specified index path was highlighted.
- [func collectionView(UICollectionView, didUnhighlightItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:didunhighlightitemat:).md)
  Tells the delegate that the highlight was removed from the item at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldhighlightitemat:))*