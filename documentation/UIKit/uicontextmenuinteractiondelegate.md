# UIContextMenuInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIContextMenuInteractionDelegate : NSObjectProtocol
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

Use this protocol to provide UIKit with the contextual menu that you want to display. When a [`UIContextMenuInteraction`](uicontextmenuinteraction.md) object detects an appropriate interaction, it calls the [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:).md) method of your delegate. You use that method to specify the basic configuration details for your interface. In addition to your contextual menu, you can tell UIKit whether you want it to display a default preview interface or a custom view controller that you provide. You can also specify options for how you want UIKit to animate the presentation and dismissal of that interface.

For additional information about how to implement contextual menus, see [`Adding context menus in your app`](adding-context-menus-in-your-app.md).

## Topics

### Providing the preview configuration data
- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configurationformenuatlocation:).md)
  Returns the configuration data to use when previewing the content.
- [class UIContextMenuConfiguration](uicontextmenuconfiguration.md)
  An object containing the configuration details for the contextual menu.
### Customizing the preview animations
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, highlightPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:highlightpreviewforitemwithidentifier:).md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [func contextMenuInteraction(UIContextMenuInteraction, configuration: UIContextMenuConfiguration, dismissalPreviewForItemWithIdentifier: any NSCopying) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:configuration:dismissalpreviewforitemwithidentifier:).md)
  Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
### Responding to the menu’s appearance
- [func contextMenuInteraction(UIContextMenuInteraction, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willperformpreviewactionformenuwith:animator:).md)
  Informs the delegate when a preview action begins.
- [protocol UIContextMenuInteractionCommitAnimating](uicontextmenuinteractioncommitanimating.md)
  Methods adopted by system-supplied animator objects when committing preview-related animations.
### Handling animations
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willdisplaymenufor:animator:).md)
  Informs the delegate when a menu display begins.
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontextmenuinteractiondelegate/contextmenuinteraction(_:willendfor:animator:).md)
  Informs the delegate when a menu display ends.
- [protocol UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md)
  Methods adopted by system-supplied animator objects when interacting with context menus.
### Deprecated
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:).md)
  Returns the source view to use when animating the appearance of the preview interface.
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:).md)
  Returns the destination view to use when animating the appearance of the preview interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIButton](uibutton.md)
- [UIColorWell](uicolorwell.md)
- [UIControl](uicontrol.md)
- [UIDatePicker](uidatepicker.md)
- [UIPageControl](uipagecontrol.md)
- [UIPasteControl](uipastecontrol.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISlider](uislider.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITextField](uitextfield.md)

## See Also

- [class UIContextMenuSystem](uicontextmenusystem.md)
  The context menu system.
- [class UIContextMenuInteraction](uicontextmenuinteraction.md)
  An interaction object that you use to display relevant actions for your content.
- [class UITargetedPreview](uitargetedpreview.md)
  An object describing the view to use during preview-related animations.
- [class UIPreviewTarget](uipreviewtarget.md)
  An object that specifies the container view to use for animations.
- [class UIPreviewParameters](uipreviewparameters.md)
  Additional parameters to use when animating a preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate)*