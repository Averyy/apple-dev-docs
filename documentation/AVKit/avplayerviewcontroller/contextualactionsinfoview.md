# contextualActionsInfoView

**Framework**: AVKit  
**Kind**: property

A view the system shows adjacent to the contextual actions that’s suitable for showing related information.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contextualActionsInfoView: UIView { get }
```

#### Discussion

Use this view to add additional metadata, information, and artwork as subviews.

## See Also

- [var infoViewActions: [UIAction]!](avplayerviewcontroller/infoviewactions.md)
  An array of actions to present in the Info content view.
- [var customInfoViewControllers: [UIViewController]](avplayerviewcontroller/custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var contextualActions: [UIAction]](avplayerviewcontroller/contextualactions.md)
  An array of action controls to present contextually during playback.
- [var contextualActionsPreviewImage: UIImage?](avplayerviewcontroller/contextualactionspreviewimage.md)
  An image to show alongside the contextual actions.
- [var requiresMonoscopicViewingMode: Bool](avplayerviewcontroller/requiresmonoscopicviewingmode.md)
  A Boolean value that indicates whether to permit playback of 2D video content only.
- [var experienceController: AVExperienceController](avplayerviewcontroller/experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactionsinfoview)*