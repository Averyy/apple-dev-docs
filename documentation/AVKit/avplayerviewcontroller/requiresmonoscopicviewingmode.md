# requiresMonoscopicViewingMode

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether to permit playback of 2D video content only.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
var requiresMonoscopicViewingMode: Bool { get set }
```

#### Discussion

The default value is `false`.

## See Also

- [var infoViewActions: [UIAction]!](avplayerviewcontroller/infoviewactions.md)
  An array of actions to present in the Info content view.
- [var customInfoViewControllers: [UIViewController]](avplayerviewcontroller/custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var contextualActions: [UIAction]](avplayerviewcontroller/contextualactions.md)
  An array of action controls to present contextually during playback.
- [var contextualActionsInfoView: UIView](avplayerviewcontroller/contextualactionsinfoview.md)
  A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [var contextualActionsPreviewImage: UIImage?](avplayerviewcontroller/contextualactionspreviewimage.md)
  An image to show alongside the contextual actions.
- [var experienceController: AVExperienceController](avplayerviewcontroller/experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresmonoscopicviewingmode)*