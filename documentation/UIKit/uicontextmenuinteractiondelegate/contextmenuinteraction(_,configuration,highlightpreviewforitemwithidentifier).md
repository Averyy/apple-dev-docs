# contextMenuInteraction(_:configuration:highlightPreviewForItemWithIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier identifier: any NSCopying) -> UITargetedPreview?
```

```objc
- (UITargetedPreview *) contextMenuInteraction:(UIContextMenuInteraction *) interaction configuration:(UIContextMenuConfiguration *) configuration highlightPreviewForItemWithIdentifier:(id<NSCopying>) identifier;
```

## Return Value

A targeted preview object corresponding to the item with the identifier to use during the menu’s highlight and presentation animation.

## Discussion

The system calls this method when a context-menu interaction begins. Implement this method to override the default highlight preview that the system generates for the item.

## Parameters

- `interaction`: The context-menu interaction object.
- `configuration`: The configuration of the menu to present if the interaction proceeds.
- `identifier`: The identifier for the item to generate a preview for.

## See Also

### Customizing the preview animations
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](./contextmenuinteraction%28_,configuration,dismissalpreviewforitemwithidentifier%29.md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewforhighlightingmenuwithconfiguration%29.md)
  Returns the source view to use when animating the appearance of the preview interface.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewfordismissingmenuwithconfiguration%29.md)
  Returns the destination view to use when animating the appearance of the preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:highlightpreviewforitemwithidentifier:))*