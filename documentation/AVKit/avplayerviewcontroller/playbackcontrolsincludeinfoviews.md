# playbackControlsIncludeInfoViews

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
var playbackControlsIncludeInfoViews: Bool { get set }
```

#### Discussion

This property determines whether the player shows views for video metadata, navigation markers, and playback settings. Set this property value to [`false`](https://developer.apple.com/documentation/swift/false), and [`showsPlaybackControls`](avplayerviewcontroller/showsplaybackcontrols.md) to [`true`](https://developer.apple.com/documentation/swift/true), to selectively prevent the player from displaying its information and setting panels. Changing the value of this property doesn’t immediately change the visibility of the info views.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var playbackControlsIncludeTransportBar: Bool](avplayerviewcontroller/playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var transportBarIncludesTitleView: Bool](avplayerviewcontroller/transportbarincludestitleview.md)
  A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [var transportBarCustomMenuItems: [UIMenuElement]](avplayerviewcontroller/transportbarcustommenuitems.md)
  An array of actions and menus to display with the default player controls.
- [var customInfoViewControllers: [UIViewController]](avplayerviewcontroller/custominfoviewcontrollers.md)
  An array of view controllers to display as content tabs in the player user interface.
- [var infoViewActions: [UIAction]!](avplayerviewcontroller/infoviewactions.md)
  An array of actions to present in the Info content view.
- [var contextualActions: [UIAction]](avplayerviewcontroller/contextualactions.md)
  An array of action controls to present contextually during playback.
- [var customOverlayViewController: UIViewController?](avplayerviewcontroller/customoverlayviewcontroller.md)
  A view controller that presents custom content over the player view.
- [var unobscuredContentGuide: UILayoutGuide](avplayerviewcontroller/unobscuredcontentguide.md)
  A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [var customInfoViewController: UIViewController?](avplayerviewcontroller/custominfoviewcontroller.md)
  A view controller that provides client-specific content and controls alongside system-provided information and settings panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/playbackcontrolsincludeinfoviews)*