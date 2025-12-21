# collectionView(_:performPrimaryActionForItemAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to perform the primary action for the cell at the specified index path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, performPrimaryActionForItemAt indexPath: IndexPath)
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single cell without extending an existing selection.

UIKit calls this method after [`collectionView(_:shouldSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md) and [`collectionView(_:didSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:didselectitemat:).md), regardless of whether the cell selection state changes. Use [`collectionView(_:didSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:didselectitemat:).md) to update the state of the current view controller (like its buttons, title, and so on), and use [`collectionView(_:performPrimaryActionForItemAt:)`](uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:).md) for actions like navigation or showing another split view column.

If [`collectionView(_:shouldSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md) returns [`true`](https://developer.apple.com/documentation/Swift/true) to allow selection for the cell at `indexPath`, only that cell has selection when the system calls this method. If [`collectionView(_:shouldSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:shouldselectitemat:).md) returns [`false`](https://developer.apple.com/documentation/Swift/false), the system preserves the existing cell selection in the collection view. You can use this behavior to perform primary actions on nonselectable, button-style cells without changing the selection.

## Parameters

- `collectionView`: The collection view object on which to perform the primary action.
- `indexPath`: The index path of the cell.

## See Also

- [func collectionView(UICollectionView, canPerformPrimaryActionForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:canperformprimaryactionforitemat:).md)
  Asks the delegate whether to perform a primary action for the cell at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:))*