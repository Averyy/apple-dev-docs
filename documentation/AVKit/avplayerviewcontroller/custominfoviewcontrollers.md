# customInfoViewControllers

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An array of view controllers to display as content tabs in the player user interface.

**Availability**:
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var customInfoViewControllers: [UIViewController] { get set }
```

```objc
@property (nonatomic, copy) NSArray<UIViewController *> * customInfoViewControllers;
```

## Mentions

- [Adopting the system player interface in visionOS](../adopting-the-system-player-interface-in-visionos.md)
- [Customizing the tvOS playback experience](../customizing-the-tvos-playback-experience.md)

## Discussion

The system uses a view controller’s [`title`](../../UIKit/uiviewcontroller/title.md) property value as the content tab title. Set this property value before adding it to the array so that the title renders correctly in the player’s user interface.

Similarly, set a [`preferredContentSize`](../../UIKit/uiviewcontroller/preferredcontentsize.md) value on the custom view controllers, or define appropriate auto layout constraints on their views, so the system sizes them correctly in the player user interface.

> ❗ **Important**:  The view with the greatest height determines the height of all of the content views. Set the height of your content views consistently to simplify layout, or verify that your content renders as intended if the system resizes it.

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
- [var infoViewActions: [UIAction]!](./infoviewactions.md)
  An array of actions to present in the Info content view.
- [var contextualActions: [UIAction]](./contextualactions.md)
  An array of action controls to present contextually during playback.
- [var customOverlayViewController: UIViewController?](./customoverlayviewcontroller.md)
  A view controller that presents custom content over the player view.
- [var unobscuredContentGuide: UILayoutGuide](./unobscuredcontentguide.md)
  A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [var customInfoViewController: UIViewController?](./custominfoviewcontroller.md)
  A view controller that provides client-specific content and controls alongside system-provided information and settings panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/custominfoviewcontrollers)*