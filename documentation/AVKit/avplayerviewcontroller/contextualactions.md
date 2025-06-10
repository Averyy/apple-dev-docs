# contextualActions

**Framework**: AVKit  
**Kind**: property

An array of action controls to present contextually during playback.

**Availability**:
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contextualActions: [UIAction] { get set }
```

## Mentions

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)

#### Discussion

Use this property to present action controls for a specific time in the presentation, such as showing a Skip Intro button during a title sequence. Have your app observe the player’s timing, and when playback reaches a point at which to present controls, set the property value to one or more custom actions. To dismiss the controls, set this property value back to an empty array.

For details about observing player timing, see `Observing the Playback Time`.

> **Note**:  The view controller presents contextual actions only when the transport bar isn’t visible.

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
- [var infoViewActions: [UIAction]!](avplayerviewcontroller/infoviewactions.md)
  An array of actions to present in the Info content view.
- [var customOverlayViewController: UIViewController?](avplayerviewcontroller/customoverlayviewcontroller.md)
  A view controller that presents custom content over the player view.
- [var unobscuredContentGuide: UILayoutGuide](avplayerviewcontroller/unobscuredcontentguide.md)
  A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [var customInfoViewController: UIViewController?](avplayerviewcontroller/custominfoviewcontroller.md)
  A view controller that provides client-specific content and controls alongside system-provided information and settings panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactions)*