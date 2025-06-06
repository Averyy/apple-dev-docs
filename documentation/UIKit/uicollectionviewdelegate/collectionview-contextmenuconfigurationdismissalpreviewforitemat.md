# collectionView(_:contextMenuConfiguration:dismissalPreviewForItemAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfiguration configuration: UIContextMenuConfiguration, dismissalPreviewForItemAt indexPath: IndexPath) -> UITargetedPreview?
```

#### Return Value

A targeted preview object corresponding to the item at the index path to use during the menu’s dismissal animation.

#### Discussion

The system calls this method when a context menu dismisses from the collection view. Implement this method to override the default dismissal preview that the collection view generates for the item at `indexPath`.

## Parameters

- `collectionView`: The collection view containing the item.
- `configuration`: The configuration of the menu to dismiss.
- `indexPath`: The index path of the item where the menu dismissal occurs.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func collectionView(UICollectionView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicollectionviewdelegate/collectionview(_:willdisplaycontextmenu:animator:).md)
  Informs the delegate when a context menu will appear.
- [func collectionView(UICollectionView, willEndContextMenuInteraction: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicollectionviewdelegate/collectionview(_:willendcontextmenuinteraction:animator:).md)
  Informs the delegate when a context menu will disappear.
- [func collectionView(UICollectionView, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](uicollectionviewdelegate/collectionview(_:willperformpreviewactionformenuwith:animator:).md)
  Informs the delegate when a user triggers a commit by tapping the preview.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemsAt: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration?](uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemsat:point:).md)
  Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, highlightPreviewForItemAt: IndexPath) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:highlightpreviewforitemat:).md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:dismissalpreviewforitemat:))*