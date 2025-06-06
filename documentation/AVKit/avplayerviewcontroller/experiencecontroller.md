# experienceController

**Framework**: AVKit  
**Kind**: property

The experience controller for this view controller.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var experienceController: AVExperienceController { get }
```

#### Discussion

Use an experience controller to transition a player to different experiences and observe experience transitions.

The use of the experience controller is mutually exclusive with a view controller’s existing API for managing the experience. After accessing the `experienceController` property, those methods will log an error and have no effect. Attempting to access this property may fail if these mutually-exclusive properties and methods have been used.

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
- [var requiresMonoscopicViewingMode: Bool](avplayerviewcontroller/requiresmonoscopicviewingmode.md)
  A Boolean value that indicates whether to permit playback of 2D video content only.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](avplayerviewcontroller/groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/experiencecontroller)*