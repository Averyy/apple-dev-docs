# showsFullScreenToggleButton

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the player view displays a full-screen toggle button.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var showsFullScreenToggleButton: Bool { get set }
```

```objc
@property BOOL showsFullScreenToggleButton;
```

## Discussion

This property is currently supported only with a [`controlsStyle`](./controlsstyle.md) of [`AVPlayerViewControlsStyle.floating`](../avplayerviewcontrolsstyle/floating.md) or [`AVPlayerViewControlsStyle.inline`](../avplayerviewcontrolsstyle/inline.md).

The default value is `false`.

## See Also

### Customizing the user interface
- [var controlsStyle: AVPlayerViewControlsStyle](./controlsstyle.md)
  The player view’s controls style.
- [enum AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md)
  Constants that indicate which user interface controls the view displays.
- [var showsFrameSteppingButtons: Bool](./showsframesteppingbuttons.md)
  A Boolean value that determines whether the player view displays frame stepping buttons.
- [var showsSharingServiceButton: Bool](./showssharingservicebutton.md)
  A Boolean value that determines whether the player view displays a sharing service button.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var contentOverlayView: NSView?](./contentoverlayview.md)
  A view that adds additional custom views between the video content and the controls.
- [var actionPopUpButtonMenu: NSMenu?](./actionpopupbuttonmenu.md)
  An action pop-up button menu that the player view displays.
- [var updatesNowPlayingInfoCenter: Bool](./updatesnowplayinginfocenter.md)
  A Boolean value that indicates whether the player view controller updates the Now Playing info center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/showsfullscreentogglebutton)*