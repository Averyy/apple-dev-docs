# collectionView(_:canFocusItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the item at the specified index path can be focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, canFocusItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the item can receive be focused or [`false`](https://developer.apple.com/documentation/Swift/false) if it can not.

#### Discussion

You can use this method, or a cell’s [`canBecomeFocused`](uiview/canbecomefocused.md) method, to control which items in the collection view can receive focus. The focus engine calls the cell’s [`canBecomeFocused`](uiview/canbecomefocused.md) method first, the default implementation of which defers to the collection view and this delegate method.

If you do not implement this method, the ability to focus on items depends on whether the collection view’s items are selectable. When the items are selectable, they can also be focused as if this method had returned [`true`](https://developer.apple.com/documentation/Swift/true); otherwise, they do not receive focus.

## Parameters

- `collectionView`: The collection view object requesting this information.
- `indexPath`: The index path of an item in the collection view.

## See Also

- [var allowsSelection: Bool](uicollectionview/allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [func indexPathForPreferredFocusedView(in: UICollectionView) -> IndexPath?](uicollectionviewdelegate/indexpathforpreferredfocusedview(in:).md)
  Asks the delegate for the index path of the cell that should be focused.
- [func collectionView(UICollectionView, shouldUpdateFocusIn: UICollectionViewFocusUpdateContext) -> Bool](uicollectionviewdelegate/collectionview(_:shouldupdatefocusin:).md)
  Asks the delegate whether a change in focus should occur.
- [func collectionView(UICollectionView, didUpdateFocusIn: UICollectionViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:).md)
  Tells the delegate that a focus update occurred.
- [func collectionView(UICollectionView, selectionFollowsFocusForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:selectionfollowsfocusforitemat:).md)
  Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canfocusitemat:))*