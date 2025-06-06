# contextMenuInteraction(_:configuration:dismissalPreviewForItemWithIdentifier:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier identifier: any NSCopying) -> UITargetedPreview?
```

#### Return Value

A targeted preview object corresponding to the item with the identifier to use during the menu’s dismissal animation.

#### Discussion

The system calls this method when a context-menu dismissal occurs. Implement this method to override the default dismissal preview that the system generates for the item.

## Parameters

- `interaction`: The context-menu interaction object.
- `configuration`: The configuration of the menu to dismiss.
- `identifier`: The identifier for the item to generate a preview for.

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:highlightpreviewforitemwithidentifier:).md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:dismissalpreviewforitemwithidentifier:))*