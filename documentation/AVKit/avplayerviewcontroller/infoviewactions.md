# infoViewActions

**Framework**: AVKit  
**Kind**: property

An array of actions to present in the Info content view.

**Availability**:
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var infoViewActions: [UIAction]! { get set }
```

## Mentions

- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)

#### Discussion

The Info content view can display up to two custom action controls along its trailing edge. The default value of this property is a single action that plays the current media from the beginning when tapped.

## See Also

- [var playbackControlsIncludeTransportBar: Bool](avplayerviewcontroller/playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var playbackControlsIncludeInfoViews: Bool](avplayerviewcontroller/playbackcontrolsincludeinfoviews.md)
  A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [var transportBarIncludesTitleView: Bool](avplayerviewcontroller/transportbarincludestitleview.md)
  A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [var transportBarCustomMenuItems: [UIMenuElement]](avplayerviewcontroller/transportbarcustommenuitems.md)
  An array of actions and menus to display with the default player controls.
- [var customInfoViewControllers: [UIViewController]](avplayerviewcontroller/custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var contextualActions: [UIAction]](avplayerviewcontroller/contextualactions.md)
  An array of action controls to present contextually during playback.
- [var customOverlayViewController: UIViewController?](avplayerviewcontroller/customoverlayviewcontroller.md)
  A view controller that presents custom content over the player view.
- [var unobscuredContentGuide: UILayoutGuide](avplayerviewcontroller/unobscuredcontentguide.md)
  A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [var customInfoViewController: UIViewController?](avplayerviewcontroller/custominfoviewcontroller.md)
  A view controller that provides client-specific content and controls alongside system-provided information and settings panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/infoviewactions)*