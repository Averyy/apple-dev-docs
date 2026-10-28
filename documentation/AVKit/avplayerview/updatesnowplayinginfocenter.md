# updatesNowPlayingInfoCenter

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player view controller updates the Now Playing info center.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var updatesNowPlayingInfoCenter: Bool { get set }
```

```objc
@property BOOL updatesNowPlayingInfoCenter;
```

## Discussion

The default value is `true`.

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
- [var showsFullScreenToggleButton: Bool](./showsfullscreentogglebutton.md)
  A Boolean value that determines whether the player view displays a full-screen toggle button.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var contentOverlayView: NSView?](./contentoverlayview.md)
  A view that adds additional custom views between the video content and the controls.
- [var actionPopUpButtonMenu: NSMenu?](./actionpopupbuttonmenu.md)
  An action pop-up button menu that the player view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/updatesnowplayinginfocenter)*