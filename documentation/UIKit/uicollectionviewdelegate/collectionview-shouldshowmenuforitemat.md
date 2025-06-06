# collectionView(_:shouldShowMenuForItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if an action menu should be displayed for the specified item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the editing menu should be shown positioned near the item and pointing to it or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

If the user tap-holds a certain item in the collection view, this method (if implemented) is invoked first. Return [`true`](https://developer.apple.com/documentation/swift/true) if you want to permit the editing menu to be displayed. Return [`false`](https://developer.apple.com/documentation/swift/false) if the editing menu shouldn’t be shown—for example, you might return [`false`](https://developer.apple.com/documentation/swift/false) if the corresponding item contains data that should not be copied or pasted over.

If you do not implement this method, the default return value is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `collectionView`: The collection view object that is making the request.
- `indexPath`: The index path of the affected item.

## See Also

- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:).md)
  Returns a context menu configuration for the item at a point.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewfordismissingcontextmenuwithconfiguration:).md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:).md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:).md)
  Asks the delegate if it can perform the specified action on an item in the collection view.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:).md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:))*