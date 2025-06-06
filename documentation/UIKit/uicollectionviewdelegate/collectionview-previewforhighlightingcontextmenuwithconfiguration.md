# collectionView(_:previewForHighlightingContextMenuWithConfiguration:)

**Framework**: UIKit  
**Kind**: method

Returns a view to override the default preview the collection view created.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, previewForHighlightingContextMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

#### Return Value

A targeted preview object describing the highlight preview.

## Parameters

- `collectionView`: The collection view object requesting this information.
- `configuration`: The configuration of the menu being highlighted.

## See Also

- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:).md)
  Returns a context menu configuration for the item at a point.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewfordismissingcontextmenuwithconfiguration:).md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:).md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:).md)
  Asks the delegate if it can perform the specified action on an item in the collection view.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:).md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:))*