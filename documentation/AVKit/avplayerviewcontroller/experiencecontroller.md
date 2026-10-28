# experienceController

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The experience controller for this view controller.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var experienceController: AVExperienceController { get }
```

## Discussion

Use an experience controller to transition a player to different experiences and observe experience transitions.

The use of the experience controller is mutually exclusive with a view controller’s existing API for managing the experience. After accessing the `experienceController` property, those methods log an error and have no effect. Attempting to access this property may fail if you use these mutually exclusive properties and methods together.

## See Also

### Configuring the visionOS player UI
- [var infoViewActions: [UIAction]!](./infoviewactions.md)
  An array of actions to present in the Info content view.
- [var customInfoViewControllers: [UIViewController]](./custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var contextualActions: [UIAction]](./contextualactions.md)
  An array of action controls to present contextually during playback.
- [var contextualActionsInfoView: UIView](./contextualactionsinfoview.md)
  A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [var contextualActionsPreviewImage: UIImage?](./contextualactionspreviewimage.md)
  An image to show alongside the contextual actions.
- [var requiresMonoscopicViewingMode: Bool](./requiresmonoscopicviewingmode.md)
  A Boolean value that indicates whether to permit playback of 2D video content only.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](./groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.
- [var viewport: AVViewport](./viewport.md)
  A configuration object that manages viewport settings for different presentation modes.
- [class AVViewport](../avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/experiencecontroller)*