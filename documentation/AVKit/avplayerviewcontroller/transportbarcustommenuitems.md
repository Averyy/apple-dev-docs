# transportBarCustomMenuItems

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An array of actions and menus to display with the default player controls.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var transportBarCustomMenuItems: [UIMenuElement] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSArray<__kindof UIMenuElement *> * transportBarCustomMenuItems;
```

## Mentions

- [Customizing the tvOS playback experience](../customizing-the-tvos-playback-experience.md)

## Discussion

Use this property to display custom pop-up menus in transport bar. This property only supports menu elements of type [`UIAction`](../../UIKit/uiaction.md) and [`UIMenu`](../../UIKit/uimenu.md), and supports displaying inline one level of submenus.

## See Also

### Customizing the tvOS player UI
- [var playbackControlsIncludeTransportBar: Bool](./playbackcontrolsincludetransportbar.md)
  A Boolean value that indicates whether the player shows the transport bar and related controls.
- [var playbackControlsIncludeInfoViews: Bool](./playbackcontrolsincludeinfoviews.md)
  A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when someone requests them.
- [var transportBarIncludesTitleView: Bool](./transportbarincludestitleview.md)
  A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/transportbarcustommenuitems)*