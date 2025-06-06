# collectionView(_:canPerformAction:forItemAt:withSender:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if it can perform the specified action on an item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the command corresponding to action should appear in the editing menu or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

This method is invoked after the [`collectionView(_:shouldShowMenuForItemAt:)`](uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:).md) method. It gives you the opportunity to exclude commands from the editing menu. For example, the user might have copied some content from one item and wants to paste it into another item that cannot accept the content. In such a case, your method could return [`false`](https://developer.apple.com/documentation/swift/false) to prevent the display of the relevant command.

If you do not implement this method, the default return value is [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `collectionView`: The collection view object that is making the request.
- `action`: The selector identifying the action to be performed.
- `indexPath`: The index path of the affected item.
- `sender`: The object that wants to initiate the action.

## See Also

- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:).md)
  Returns a context menu configuration for the item at a point.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewfordismissingcontextmenuwithconfiguration:).md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:).md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:).md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:).md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:))*