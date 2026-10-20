# collectionView(_:contextMenuConfigurationForItemAt:point:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a context menu configuration for the item at a point.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`collectionView(_:contextMenuConfigurationForItemsAt:point:)`](./collectionview%28_,contextmenuconfigurationforitemsat,point%29.md) instead.

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?
```

```objc
- (UIContextMenuConfiguration *) collectionView:(UICollectionView *) collectionView contextMenuConfigurationForItemAtIndexPath:(NSIndexPath *) indexPath point:(CGPoint) point;
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

### Deprecated methods
- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](./collectionview%28_,targetindexpathformovefromitemat,toproposedindexpath%29.md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./collectionview%28_,previewfordismissingcontextmenuwithconfiguration%29.md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./collectionview%28_,previewforhighlightingcontextmenuwithconfiguration%29.md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](./collectionview%28_,shouldshowmenuforitemat%29.md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](./collectionview%28_,canperformaction,foritemat,withsender%29.md)
  Asks the delegate if it can perform the specified action on an item in the collection view.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](./collectionview%28_,performaction,foritemat,withsender%29.md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemat:point:))*