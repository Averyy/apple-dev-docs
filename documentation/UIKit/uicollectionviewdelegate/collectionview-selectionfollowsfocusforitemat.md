# collectionView(_:selectionFollowsFocusForItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, selectionFollowsFocusForItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you want to automatically select the cell at the specified index path when focus moves to it; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the collection view’s [`selectionFollowsFocus`](uicollectionview/selectionfollowsfocus.md) property is [`true`](https://developer.apple.com/documentation/Swift/true) and you return [`false`](https://developer.apple.com/documentation/Swift/false) from this delegate method, focus still moves to the cell when the user selects it. However, when focus moves to the cell, the cell doesn’t automatically select.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPath`: The index path of the cell to determine selection and focus behavior for.

## See Also

- [func collectionView(UICollectionView, canFocusItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:canfocusitemat:).md)
  Asks the delegate whether the item at the specified index path can be focused.
- [func indexPathForPreferredFocusedView(in: UICollectionView) -> IndexPath?](uicollectionviewdelegate/indexpathforpreferredfocusedview(in:).md)
  Asks the delegate for the index path of the cell that should be focused.
- [func collectionView(UICollectionView, shouldUpdateFocusIn: UICollectionViewFocusUpdateContext) -> Bool](uicollectionviewdelegate/collectionview(_:shouldupdatefocusin:).md)
  Asks the delegate whether a change in focus should occur.
- [func collectionView(UICollectionView, didUpdateFocusIn: UICollectionViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:).md)
  Tells the delegate that a focus update occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:selectionfollowsfocusforitemat:))*