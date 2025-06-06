# collectionView(_:contextMenuConfigurationForItemsAt:point:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a context-menu configuration for the items at the specified index paths.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemsAt indexPaths: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration?
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Return Value

A contextual menu configuration object describing the menu to present. Returning `nil` prevents the interaction from beginning. Returning an empty configuration causes the interaction to begin, and then end with a cancellation effect. You can use this cancellation effect to indicate to people that it’s possible to present a menu from this element, but that there aren’t any actions currently available.

#### Discussion

The system calls this method when a person invokes a context menu from the collection view. Implement this method to build a [`UIContextMenuConfiguration`](uicontextmenuconfiguration.md) according to the index paths the system passes in to this method. The following code example shows different context-menu configurations for zero, one, and multiple index paths.

```swift
func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemsAt indexPaths: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(actionProvider: { suggestedActions in
        if indexPaths.count == 0 {
            // Construct an empty-space menu.
            return UIMenu(children: [
                UIAction(title: "New Folder") { _ in /* Implement the action. */ }
            ])
        }
        else if indexPaths.count == 1 {
            // Construct a single-item menu.
            return UIMenu(children: [
                UIAction(title: "Copy") { _ in /* Implement the action. */ },
                UIAction(title: "Delete", attributes: .destructive) { _ in /* Implement the action. */ }
            ])
        }
        else {
            // Construct a multiple-item menu.
            return UIMenu(children: [
                UIAction(title: "New Folder With Selection") { _ in /* Implement the action. */ }
            ])
        }
    })
}
```

## Parameters

- `collectionView`: The collection view containing the items.
- `indexPaths`: An array of index paths corresponding to the items the menu acts on. An empty array indicates that a person is invoking the menu from a location that doesn’t map to an item index path, like the space between cells. An array with multiple index paths indicates that a person is invoking the menu on an item in a multiple selection.
- `point`: The location of the interaction in the collection view’s coordinate space.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func collectionView(UICollectionView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicollectionviewdelegate/collectionview(_:willdisplaycontextmenu:animator:).md)
  Informs the delegate when a context menu will appear.
- [func collectionView(UICollectionView, willEndContextMenuInteraction: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicollectionviewdelegate/collectionview(_:willendcontextmenuinteraction:animator:).md)
  Informs the delegate when a context menu will disappear.
- [func collectionView(UICollectionView, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](uicollectionviewdelegate/collectionview(_:willperformpreviewactionformenuwith:animator:).md)
  Informs the delegate when a user triggers a commit by tapping the preview.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, highlightPreviewForItemAt: IndexPath) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:highlightpreviewforitemat:).md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, dismissalPreviewForItemAt: IndexPath) -> UITargetedPreview?](uicollectionviewdelegate/collectionview(_:contextmenuconfiguration:dismissalpreviewforitemat:).md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemsat:point:))*