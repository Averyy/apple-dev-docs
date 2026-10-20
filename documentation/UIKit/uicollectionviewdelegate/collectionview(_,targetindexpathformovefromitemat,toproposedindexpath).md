# collectionView(_:targetIndexPathForMoveFromItemAt:toProposedIndexPath:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the index path to use when moving an item.

**Availability**:
- iOS 9.0+ - Deprecated in 15.0
- iPadOS 9.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`collectionView(_:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:)`](./collectionview%28_,targetindexpathformoveofitemfromoriginalindexpath,atcurrentindexpath,toproposedindexpath%29.md) instead.

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveFromItemAt currentIndexPath: IndexPath, toProposedIndexPath proposedIndexPath: IndexPath) -> IndexPath
```

```objc
- (NSIndexPath *) collectionView:(UICollectionView *) collectionView targetIndexPathForMoveFromItemAtIndexPath:(NSIndexPath *) currentIndexPath toProposedIndexPath:(NSIndexPath *) proposedIndexPath;
```

#### Return Value

The index path you want to use for the item. If you do not implement this method, the collection view uses the index path in the `proposedIndexPath` parameter.

#### Discussion

During the interactive moving of an item, the collection view calls this method to see if you want to provide a different index path than the proposed path. You might use this method to prevent the user from dropping the item in an invalid location. For example, you might prevent the user from dropping the item in a specific section.

## Parameters

- `collectionView`: The collection view making the request.
- `currentIndexPath`: The item’s original index path.
- `proposedIndexPath`: The proposed index path of the item.

## See Also

### Deprecated methods
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
- [func collectionView(UICollectionView, performAction: Selector, forItemAt: IndexPath, withSender: Any?)](./collectionview%28_,performaction,foritemat,withsender%29.md)
  Tells the delegate to perform the specified action on an item in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:))*