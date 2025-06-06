# collectionView(_:contextMenuConfigurationForItemAt:point:)

**Framework**: UIKit  
**Kind**: method

Returns a context menu configuration for the item at a point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?
```

#### Return Value

A contextual menu configuration object describing the menu to be presented. Returning `nil` prevents the interaction from beginning. Returning an empty configuration object causes the interaction to begin, and then end with a cancellation effect.

#### Discussion

You can use the cancellation effect from returning an empty configuration to indicate to users that it’s possible for a menu to be presented from this item, but that there are no actions to present at this particular time.

## Parameters

- `collectionView`: The collection view containing the item.
- `indexPath`: The index path of the item for which a configuration is being requested.
- `point`: The location of the interaction in the collection view’s coordinate space.

## See Also

- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:).md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewfordismissingcontextmenuwithconfiguration:).md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:previewforhighlightingcontextmenuwithconfiguration:).md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:shouldshowmenuforitemat:).md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:).md)
  Asks the delegate if it can perform the specified action on an item in the collection view.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:).md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:))*