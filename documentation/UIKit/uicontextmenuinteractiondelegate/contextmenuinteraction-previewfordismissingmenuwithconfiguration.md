# contextMenuInteraction(_:previewForDismissingMenuWithConfiguration:)

**Framework**: UIKit  
**Kind**: method

Returns the destination view to use when animating the appearance of the preview interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, previewForDismissingMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

#### Return Value

An object containing the destination view and configuration parameters for the animation.

#### Discussion

When the user dismisses the preview interface, UIKit animates that interface to the view you specify in the returned [`UITargetedPreview`](uitargetedpreview.md) object.

## Parameters

- `interaction`: The interaction object that triggered the preview.
- `configuration`: The configuration object associated with the current interaction.

## See Also

- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:).md)
  Returns the source view to use when animating the appearance of the preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:))*