# collectionView(_:performAction:forItemAt:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to perform the specified action on an item in the collection view.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView performAction:(SEL) action forItemAtIndexPath:(NSIndexPath *) indexPath withSender:(id) sender;
```

## Discussion

If the user taps an action in the editing menu, the collection view calls this method. Your implementation of this method should do whatever is appropriate for the action. For example, for a copy action, it should extract the relevant item content and write it to the general pasteboard or an application (private) pasteboard.

For information about how to perform pasteboard-related operations, see [`UIPasteboard`](../uipasteboard.md).

## Parameters

- `collectionView`: The collection view object that is making the request.
- `action`: The selector representing the action to be performed.
- `indexPath`: The index path of the affected item.
- `sender`: The object that initiated the action.

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
- [func collectionView(UICollectionView, canPerformAction: Selector, forItemAt: IndexPath, withSender: Any?) -> Bool](./collectionview%28_,canperformaction,foritemat,withsender%29.md)
  Asks the delegate if it can perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performaction:foritemat:withsender:))*