# UIInteraction

**Framework**: UIKit  
**Kind**: protocol

The protocol that an interaction implements to access the view that owns it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIInteraction : NSObjectProtocol
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

## Topics

### Getting the View
- [var view: UIView?](uiinteraction/view.md)
  The view that owns the interaction.
### Tracking the Movements
- [func didMove(to: UIView?)](uiinteraction/didmove(to:).md)
  Tells the interaction that a view added or removed it from the view’s interactions array.
- [func willMove(to: UIView?)](uiinteraction/willmove(to:).md)
  Tells the interaction that a view will add or remove it from the view’s interactions array.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIBandSelectionInteraction](uibandselectioninteraction.md)
- [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md)
- [UIContextMenuInteraction](uicontextmenuinteraction.md)
- [UIDragInteraction](uidraginteraction.md)
- [UIDropInteraction](uidropinteraction.md)
- [UIEditMenuInteraction](uieditmenuinteraction.md)
- [UIFeedbackGenerator](uifeedbackgenerator.md)
- [UIFindInteraction](uifindinteraction.md)
- [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md)
- [UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md)
- [UILargeContentViewerInteraction](uilargecontentviewerinteraction.md)
- [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md)
- [UIPencilInteraction](uipencilinteraction.md)
- [UIPointerInteraction](uipointerinteraction.md)
- [UIScribbleInteraction](uiscribbleinteraction.md)
- [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md)
- [UISpringLoadedInteraction](uispringloadedinteraction.md)
- [UITextInteraction](uitextinteraction.md)
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
- [UIToolTipInteraction](uitooltipinteraction.md)
- [UIWindowScene.ActivationInteraction](uiwindowscene/activationinteraction.md)
- [UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md)
- [UIWritingToolsCoordinator](uiwritingtoolscoordinator.md)

## See Also

- [func addInteraction(any UIInteraction)](uiview/addinteraction(_:).md)
  Adds an interaction to the view.
- [func removeInteraction(any UIInteraction)](uiview/removeinteraction(_:).md)
  Removes an interaction from the view.
- [var interactions: [any UIInteraction]](uiview/interactions.md)
  The array of interactions for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinteraction)*