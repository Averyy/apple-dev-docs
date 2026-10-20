# collectionView(_:canPerformAction:forItemAt:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if it can perform the specified action on an item in the collection view.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?) -> Bool
```

```objc
- (BOOL) collectionView:(UICollectionView *) collectionView canPerformAction:(SEL) action forItemAtIndexPath:(NSIndexPath *) indexPath withSender:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the command corresponding to action should appear in the editing menu or [`false`](../../Swift/false.md) if it should not.

#### Discussion

This method is invoked after the [`collectionView(_:shouldShowMenuForItemAt:)`](./collectionview%28_,shouldshowmenuforitemat%29.md) method. It gives you the opportunity to exclude commands from the editing menu. For example, the user might have copied some content from one item and wants to paste it into another item that cannot accept the content. In such a case, your method could return [`false`](../../Swift/false.md) to prevent the display of the relevant command.

If you do not implement this method, the default return value is [`false`](../../Swift/false.md).

## Parameters

- `collectionView`: The collection view object that is making the request.
- `action`: The selector identifying the action to be performed.
- `indexPath`: The index path of the affected item.
- `sender`: The object that wants to initiate the action.

## See Also

### Deprecated methods
- [func collectionView(UICollectionView, targetIndexPathForMoveFromItemAt: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](./collectionview%28_,targetindexpathformovefromitemat,toproposedindexpath%29.md)
  Asks the delegate for the index path to use when moving an item.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](./collectionview%28_,contextmenuconfigurationforitemat,point%29.md)
  Returns a context menu configuration for the item at a point.
- [func collectionView(UICollectionView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./collectionview%28_,previewfordismissingcontextmenuwithconfiguration%29.md)
  Returns the destination view when dismissing a context menu.
- [func collectionView(UICollectionView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./collectionview%28_,previewforhighlightingcontextmenuwithconfiguration%29.md)
  Returns a view to override the default preview the collection view created.
- [func collectionView(UICollectionView, shouldShowMenuForItemAt: IndexPath) -> Bool](./collectionview%28_,shouldshowmenuforitemat%29.md)
  Asks the delegate if an action menu should be displayed for the specified item.
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](./collectionview%28_,performaction,foritemat,withsender%29.md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformaction:foritemat:withsender:))*