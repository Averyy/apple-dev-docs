# playbackControlsIncludeInfoViews

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when someone requests them.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
var playbackControlsIncludeInfoViews: Bool { get set }
```

```objc
@property (nonatomic) BOOL playbackControlsIncludeInfoViews;
```

#### Discussion

This property determines whether the player shows views for video metadata, navigation markers, and playback settings. Set this property value to `false`, and [`showsPlaybackControls`](./showsplaybackcontrols.md) to `true`, to selectively prevent the player from displaying its information and setting panels. Changing the value of this property doesn’t immediately change the visibility of the info views.

The default value is `true`.

## See Also

### Customizing the tvOS player UI
- [var playbackControlsIncludeTransportBar: Bool](./playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
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
- [var customInfoViewController: UIViewController?](./custominfoviewcontroller.md)
  A view controller that provides client-specific content and controls alongside system-provided information and settings panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/playbackcontrolsincludeinfoviews)*