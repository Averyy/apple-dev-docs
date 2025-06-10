# transportBarIncludesTitleView

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player user interface shows the title view above the scrubber.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
@MainActor
var transportBarIncludesTitleView: Bool { get set }
```

## Mentions

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)

#### Discussion

By default, the player presents a title view. This view displays title ([`commonIdentifierTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/commonIdentifierTitle)) and subtitle ([`iTunesMetadataTrackSubTitle`](https://developer.apple.com/documentation/AVFoundation/AVMetadataIdentifier/iTunesMetadataTrackSubTitle)) metadata embedded in a media asset or set as a player item’s [`externalMetadata`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/externalMetadata).

The view controller ignores this property when [`playbackControlsIncludeTransportBar`](avplayerviewcontroller/playbackcontrolsincludetransportbar.md) is `false`.

## See Also

- [var playbackControlsIncludeTransportBar: Bool](avplayerviewcontroller/playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var playbackControlsIncludeInfoViews: Bool](avplayerviewcontroller/playbackcontrolsincludeinfoviews.md)
  A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/transportbarincludestitleview)*