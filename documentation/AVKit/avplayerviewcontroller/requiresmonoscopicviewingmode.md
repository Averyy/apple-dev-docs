# requiresMonoscopicViewingMode

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to permit playback of 2D video content only.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var requiresMonoscopicViewingMode: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresMonoscopicViewingMode;
```

## Discussion

The default value is `false`.

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
- [var experienceController: AVExperienceController](./experiencecontroller.md)
  The experience controller for this view controller.
- [var groupExperienceCoordinator: AVGroupExperienceCoordinator](./groupexperiencecoordinator.md)
  The group experience coordinator for this view controller.
- [var viewport: AVViewport](./viewport.md)
  A configuration object that manages viewport settings for different presentation modes.
- [class AVViewport](../avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresmonoscopicviewingmode)*