# collectionView(_:canPerformPrimaryActionForItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to perform a primary action for the cell at the specified index path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, canPerformPrimaryActionForItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the primary action can be performed; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). If you don’t implement this method, the default return value is [`true`](https://developer.apple.com/documentation/swift/true) when the collection view isn’t in an editing state, and [`false`](https://developer.apple.com/documentation/swift/false) when it is.

#### Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single cell without extending an existing selection.

UIKit calls this method before [`collectionView(_:performPrimaryActionForItemAt:)`](uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:).md).

## Parameters

- `collectionView`: The collection view object asking whether to perform a primary action.
- `indexPath`: The index path of the cell.

## See Also

- [func collectionView(UICollectionView, performPrimaryActionForItemAt: IndexPath)](uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:).md)
  Tells the delegate to perform the primary action for the cell at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformprimaryactionforitemat:))*