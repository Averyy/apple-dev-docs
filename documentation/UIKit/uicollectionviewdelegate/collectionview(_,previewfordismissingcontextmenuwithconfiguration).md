# collectionView(_:previewForDismissingContextMenuWithConfiguration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the destination view when dismissing a context menu.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`collectionView(_:contextMenuConfiguration:dismissalPreviewForItemAt:)`](./collectionview%28_,contextmenuconfiguration,dismissalpreviewforitemat%29.md) instead.

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, previewForDismissingContextMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

```objc
- (UITargetedPreview *) collectionView:(UICollectionView *) collectionView previewForDismissingContextMenuWithConfiguration:(UIContextMenuConfiguration *) configuration;
```

## Return Value

A targeted preview object describing the dismissal preview. The interaction animates the presented menu to the preview. Use this method to customize the dismissal animation.

## Parameters

- `collectionView`: The collection view object requesting this information.
- `configuration`: The configuration of the menu being displayed.

## See Also

### Deprecated methods
- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](./collectionview%28_,targetindexpathformovefromitemat,toproposedindexpath%29.md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](./collectionview%28_,contextmenuconfigurationforitemat,point%29.md)
  Returns a context menu configuration for the item at a point.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./collectionview%28_,previewforhighlightingcontextmenuwithconfiguration%29.md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](./collectionview%28_,shouldshowmenuforitemat%29.md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](./collectionview%28_,canperformaction,foritemat,withsender%29.md)
  Asks the delegate if it can perform the specified action on an item in the collection view.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](./collectionview%28_,performaction,foritemat,withsender%29.md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:previewfordismissingcontextmenuwithconfiguration:))*