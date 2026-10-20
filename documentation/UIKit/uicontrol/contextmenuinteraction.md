# contextMenuInteraction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A context menu interaction for the control.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var contextMenuInteraction: UIContextMenuInteraction? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIContextMenuInteraction * contextMenuInteraction;
```

#### Discussion

This property returns a [`UIContextMenuInteraction`](../uicontextmenuinteraction.md) with the control set as its delegate. Before constructing the context menu interaction, the control verifies that it can serve as a viable delegate.

## See Also

### Managing context menus
- [Adding context menus in your app](../adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [var isContextMenuInteractionEnabled: Bool](./iscontextmenuinteractionenabled.md)
  A Boolean value that determines whether the control enables its context menu interaction.
- [var showsMenuAsPrimaryAction: Bool](./showsmenuasprimaryaction.md)
  A Boolean value that determines whether the context menu interaction is the control’s primary action.
- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](./contextmenuinteraction%28_,configurationformenuatlocation%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewfordismissingmenuwithconfiguration%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewforhighlightingmenuwithconfiguration%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./contextmenuinteraction%28_,willdisplaymenufor,animator%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./contextmenuinteraction%28_,willendfor,animator%29.md)
- [func menuAttachmentPoint(for: UIContextMenuConfiguration) -> CGPoint](./menuattachmentpoint%28for%29.md)
  Return a point in this control’s coordinate space to which to attach the given configuration’s menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/contextmenuinteraction)*