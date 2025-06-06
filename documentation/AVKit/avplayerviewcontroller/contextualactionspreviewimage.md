# contextualActionsPreviewImage

**Framework**: AVKit  
**Kind**: property

An image to show alongside the contextual actions.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var contextualActionsPreviewImage: UIImage? { get set }
```

#### Discussion

Use this to enhance a contextual action with more context. For example, if the action presents a button to jump back in time, show a preview frame of where in the movie the action skips to.

> **Note**:  The system only displays an image if the [`contextualActions`](avplayerviewcontroller/contextualactions.md) property contains a single value.

 The system only displays an image if the [`contextualActions`](avplayerviewcontroller/contextualactions.md) property contains a single value.

## See Also

- [var infoViewActions: [UIAction]!](avplayerviewcontroller/infoviewactions.md)
  An array of actions to present in the Info content view.
- [var customInfoViewControllers: [UIViewController]](avplayerviewcontroller/custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var contextualActions: [UIAction]](avplayerviewcontroller/contextualactions.md)
  An array of action controls to present contextually during playback.
- [var contextualActionsInfoView: UIView](avplayerviewcontroller/contextualactionsinfoview.md)
  A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [var requiresMonoscopicViewingMode: Bool](avplayerviewcontroller/requiresmonoscopicviewingmode.md)
  A Boolean value that indicates whether to permit playback of 2D video content only.
- [var experienceController: AVExperienceController](avplayerviewcontroller/experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactionspreviewimage)*