# contextualActionsPreviewImage

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An image to show alongside the contextual actions.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var contextualActionsPreviewImage: UIImage? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIImage * contextualActionsPreviewImage;
```

#### Discussion

Use this to enhance a contextual action with more context. For example, if the action presents a button to jump back in time, show a preview frame of where in the movie the action skips to.

> **Note**:  The system only displays an image if the [`contextualActions`](./contextualactions.md) property contains a single value.

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
- [var requiresMonoscopicViewingMode: Bool](./requiresmonoscopicviewingmode.md)
  A Boolean value that indicates whether to permit playback of 2D video content only.
- [var experienceController: AVExperienceController](./experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](./groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.
- [var viewport: AVViewport](./viewport.md)
  A configuration object that manages viewport settings for different presentation modes.
- [class AVViewport](../avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactionspreviewimage)*