# contextMenuInteraction(_:previewForDismissingMenuWithConfiguration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the destination view to use when animating the appearance of the preview interface.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`contextMenuInteraction(_:configuration:dismissalPreviewForItemWithIdentifier:)`](./contextmenuinteraction%28_,configuration,dismissalpreviewforitemwithidentifier%29.md) instead.

## Declaration

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, previewForDismissingMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

```objc
- (UITargetedPreview *) contextMenuInteraction:(UIContextMenuInteraction *) interaction previewForDismissingMenuWithConfiguration:(UIContextMenuConfiguration *) configuration;
```

## Return Value

An object containing the destination view and configuration parameters for the animation.

## Discussion

When the user dismisses the preview interface, UIKit animates that interface to the view you specify in the returned [`UITargetedPreview`](../uitargetedpreview.md) object.

## Parameters

- `interaction`: The interaction object that triggered the preview.
- `configuration`: The configuration object associated with the current interaction.

## See Also

### Customizing the preview animations
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](./contextmenuinteraction%28_,configuration,highlightpreviewforitemwithidentifier%29.md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](./contextmenuinteraction%28_,configuration,dismissalpreviewforitemwithidentifier%29.md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewforhighlightingmenuwithconfiguration%29.md)
  Returns the source view to use when animating the appearance of the preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:))*