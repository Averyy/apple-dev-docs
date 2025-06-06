# contextMenuInteraction(_:willEndFor:animator:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contextMenuInteraction(_ interaction: UIContextMenuInteraction, willEndFor configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [var contextMenuInteraction: UIContextMenuInteraction?](uicontrol/contextmenuinteraction.md)
  A context menu interaction for the control.
- [var isContextMenuInteractionEnabled: Bool](uicontrol/iscontextmenuinteractionenabled.md)
  A Boolean value that determines whether the control enables its context menu interaction.
- [var showsMenuAsPrimaryAction: Bool](uicontrol/showsmenuasprimaryaction.md)
  A Boolean value that determines whether the context menu interaction is the control’s primary action.
- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](uicontrol/contextmenuinteraction(_:configurationformenuatlocation:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontrol/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontrol/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontrol/contextmenuinteraction(_:willdisplaymenufor:animator:).md)
- [func menuAttachmentPoint(for: UIContextMenuConfiguration) -> CGPoint](uicontrol/menuattachmentpoint(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/contextmenuinteraction(_:willendfor:animator:))*