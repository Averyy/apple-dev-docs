# customInfoViewController

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A view controller that provides client-specific content and controls alongside system-provided information and settings panels.

**Availability**:
- tvOS 11.0+ - Deprecated in 15.0

> **Deprecated**: Use [`customInfoViewControllers`](./custominfoviewcontrollers.md) instead.

## Declaration

```swift
var customInfoViewController: UIViewController? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIViewController * customInfoViewController;
```

## Discussion

Use [`preferredContentSize`](../../UIKit/uiviewcontroller/preferredcontentsize.md) to provide the desired view size for the view.

## See Also

### Customizing the tvOS player UI
- [var playbackControlsIncludeTransportBar: Bool](./playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var playbackControlsIncludeInfoViews: Bool](./playbackcontrolsincludeinfoviews.md)
  A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when someone requests them.
- [var transportBarIncludesTitleView: Bool](./transportbarincludestitleview.md)
  A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [var transportBarCustomMenuItems: [UIMenuElement]](./transportbarcustommenuitems.md)
  An array of actions and menus to display with the default player controls.
- [var customInfoViewControllers: [UIViewController]](./custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var infoViewActions: [UIAction]!](./infoviewactions.md)
  An array of actions to present in the Info content view.
- [var contextualActions: [UIAction]](./contextualactions.md)
  An array of action controls to present contextually during playback.
- [var customOverlayViewController: UIViewController?](./customoverlayviewcontroller.md)
  A view controller that presents custom content over the player view.
- [var unobscuredContentGuide: UILayoutGuide](./unobscuredcontentguide.md)
  A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/custominfoviewcontroller)*