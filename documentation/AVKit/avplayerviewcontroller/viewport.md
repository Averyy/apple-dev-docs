# viewport

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A configuration object that manages viewport settings for different presentation modes.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
var viewport: AVViewport { get }
```

```objc
@property (nonatomic, strong, readonly) AVViewport * viewport;
```

## Discussion

Set [`portal`](../avviewport/portal.md) to control the aspect ratio of the frame the system uses for a portal presentation. When you don’t specify an aspect ratio, the portal defaults to 16:9 (1.78).

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
- [var experienceController: AVExperienceController](./experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](./groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.
- [class AVViewport](../avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/viewport)*