# contextMenuInteraction(_:previewForHighlightingMenuWithConfiguration:)

**Framework**: UIKit  
**Kind**: method

Returns the source view to use when animating the appearance of the preview interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

#### Return Value

An object containing the source view and configuration parameters for the animation.

#### Discussion

UIKit calls this method before an interaction begins, to give you an opportunity to supply a custom source view for the presentation animations. If you didn’t provide a preview handler block in the `configuration` data, UIKit displays the specified view in the preview interface.

## Parameters

- `interaction`: The interaction object that triggered the preview.
- `configuration`: The configuration object associated with the current interaction.

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:).md)
  Returns the destination view to use when animating the appearance of the preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:))*