# collectionView(_:performAction:forItemAt:withSender:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate to perform the specified action on an item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?)
```

#### Discussion

If the user taps an action in the editing menu, the collection view calls this method. Your implementation of this method should do whatever is appropriate for the action. For example, for a copy action, it should extract the relevant item content and write it to the general pasteboard or an application (private) pasteboard.

For information about how to perform pasteboard-related operations, see [`UIPasteboard`](uipasteboard.md).

## Parameters

- `collectionView`: The collection view object that is making the request.
- `action`: The selector representing the action to be performed.
- `indexPath`: The index path of the affected item.
- `sender`: The object that initiated the action.

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
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:).md)
  Asks the delegate if it can perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:))*