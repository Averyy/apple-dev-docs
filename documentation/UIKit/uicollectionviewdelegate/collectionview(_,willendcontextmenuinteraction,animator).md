# collectionView(_:willEndContextMenuInteraction:animator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when a context menu will disappear.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, willEndContextMenuInteraction configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView willEndContextMenuInteractionWithConfiguration:(UIContextMenuConfiguration *) configuration animator:(id<UIContextMenuInteractionAnimating>) animator;
```

## Parameters

- `collectionView`: The collection view that informs the delegate of this event.
- `configuration`: The ending configuration.
- `animator`: The animations to run alongside the disappearance transition.

## See Also

### Managing context menus
- [Adding context menus in your app](../adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func collectionView(UICollectionView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./collectionview%28_,willdisplaycontextmenu,animator%29.md)
  Informs the delegate when a context menu will appear.
- [func collectionView(UICollectionView, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](./collectionview%28_,willperformpreviewactionformenuwith,animator%29.md)
  Informs the delegate when a user triggers a commit by tapping the preview.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemsAt: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration?](./collectionview%28_,contextmenuconfigurationforitemsat,point%29.md)
  Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, highlightPreviewForItemAt: IndexPath) -> UITargetedPreview?](./collectionview%28_,contextmenuconfiguration,highlightpreviewforitemat%29.md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, dismissalPreviewForItemAt: IndexPath) -> UITargetedPreview?](./collectionview%28_,contextmenuconfiguration,dismissalpreviewforitemat%29.md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willendcontextmenuinteraction:animator:))*