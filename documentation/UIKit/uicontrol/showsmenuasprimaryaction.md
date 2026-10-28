# showsMenuAsPrimaryAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the context menu interaction is the control’s primary action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var showsMenuAsPrimaryAction: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL showsMenuAsPrimaryAction;
```

## Discussion

If this value is [`true`](../../Swift/true.md), the [`contextMenuInteraction`](./contextmenuinteraction.md) becomes the primary action of the control, and the menu shows in response to the [`touchDown`](./event/touchdown.md) event.

The default value is [`false`](../../Swift/false.md).

## See Also

### Managing context menus
- [Adding context menus in your app](../adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [var contextMenuInteraction: UIContextMenuInteraction?](./contextmenuinteraction.md)
  A context menu interaction for the control.
- [var isContextMenuInteractionEnabled: Bool](./iscontextmenuinteractionenabled.md)
  A Boolean value that determines whether the control enables its context menu interaction.
- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](./contextmenuinteraction%28_,configurationformenuatlocation%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewfordismissingmenuwithconfiguration%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./contextmenuinteraction%28_,previewforhighlightingmenuwithconfiguration%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./contextmenuinteraction%28_,willdisplaymenufor,animator%29.md)
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./contextmenuinteraction%28_,willendfor,animator%29.md)
- [func menuAttachmentPoint(for: UIContextMenuConfiguration) -> CGPoint](./menuattachmentpoint%28for%29.md)
  Return a point in this control’s coordinate space to which to attach the given configuration’s menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction)*