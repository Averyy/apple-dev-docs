# transportBarIncludesTitleView

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player user interface shows the title view above the scrubber.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var transportBarIncludesTitleView: Bool { get set }
```

```objc
@property (nonatomic) BOOL transportBarIncludesTitleView;
```

## Mentions

- [Customizing the tvOS playback experience](../customizing-the-tvos-playback-experience.md)

## Discussion

By default, the player presents a title view. This view displays title ([`commonIdentifierTitle`](../../AVFoundation/avmetadataidentifier/commonidentifiertitle.md)) and subtitle ([`iTunesMetadataTrackSubTitle`](../../AVFoundation/avmetadataidentifier/itunesmetadatatracksubtitle.md)) metadata embedded in a media asset or set as a player item’s [`externalMetadata`](../../AVFoundation/avplayeritem/externalmetadata.md).

The view controller ignores this property when [`playbackControlsIncludeTransportBar`](./playbackcontrolsincludetransportbar.md) is `false`.

## See Also

### Customizing the tvOS player UI
- [var playbackControlsIncludeTransportBar: Bool](./playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var playbackControlsIncludeInfoViews: Bool](./playbackcontrolsincludeinfoviews.md)
  A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when someone requests them.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/transportbarincludestitleview)*