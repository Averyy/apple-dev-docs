# contextMenuInteraction(_:configuration:dismissalPreviewForItemWithIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier identifier: any NSCopying) -> UITargetedPreview?
```

```objc
- (UITargetedPreview *) contextMenuInteraction:(UIContextMenuInteraction *) interaction configuration:(UIContextMenuConfiguration *) configuration dismissalPreviewForItemWithIdentifier:(id<NSCopying>) identifier;
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

### Customizing the preview animations
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](./contextmenuinteraction%28_,configuration,highlightpreviewforitemwithidentifier%29.md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewforhighlightingmenuwithconfiguration%29.md)
  Returns the source view to use when animating the appearance of the preview interface.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewfordismissingmenuwithconfiguration%29.md)
  Returns the destination view to use when animating the appearance of the preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:dismissalpreviewforitemwithidentifier:))*