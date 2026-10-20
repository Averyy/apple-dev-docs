# controlsStyle

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The player view’s controls style.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var controlsStyle: AVPlayerViewControlsStyle { get set }
```

```objc
@property AVPlayerViewControlsStyle controlsStyle;
```

#### Discussion

The player view supports several different control styles that you can use to customize the player view’s appearance and behavior. See [`AVPlayerViewControlsStyle`](../avplayerviewcontrolsstyle.md) for the possible values.

## See Also

### Customizing the user interface
- [enum AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md)
  Constants that indicate which user interface controls the view displays.
- [var showsFrameSteppingButtons: Bool](./showsframesteppingbuttons.md)
  A Boolean value that determines whether the player view displays frame stepping buttons.
- [var showsSharingServiceButton: Bool](./showssharingservicebutton.md)
  A Boolean value that determines whether the player view displays a sharing service button.
- [var showsFullScreenToggleButton: Bool](./showsfullscreentogglebutton.md)
  A Boolean value that determines whether the player view displays a full-screen toggle button.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var contentOverlayView: NSView?](./contentoverlayview.md)
  A view that adds additional custom views between the video content and the controls.
- [var actionPopUpButtonMenu: NSMenu?](./actionpopupbuttonmenu.md)
  An action pop-up button menu that the player view displays.
- [var updatesNowPlayingInfoCenter: Bool](./updatesnowplayinginfocenter.md)
  A Boolean value that indicates whether the player view controller updates the Now Playing info center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/controlsstyle)*