# actionPopUpButtonMenu

**Framework**: AVKit  
**Kind**: property

An action pop-up button menu that the player view displays.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@IBOutlet
@MainActor var actionPopUpButtonMenu: NSMenu? { get set }
```

#### Discussion

Set this property value to show an action pop-up button. Setting a custom action pop-up button is currently supported only for a [`controlsStyle`](avplayerview/controlsstyle.md) of [`AVPlayerViewControlsStyle.floating`](avplayerviewcontrolsstyle/floating.md) or [`AVPlayerViewControlsStyle.inline`](avplayerviewcontrolsstyle/inline.md).

The default value is `nil`.

## See Also

- [var controlsStyle: AVPlayerViewControlsStyle](avplayerview/controlsstyle.md)
  The player view’s controls style.
- [enum AVPlayerViewControlsStyle](avplayerviewcontrolsstyle.md)
  Constants that indicate which user interface controls the view displays.
- [var showsFrameSteppingButtons: Bool](avplayerview/showsframesteppingbuttons.md)
  A Boolean value that determines whether the player view displays frame stepping buttons.
- [var showsSharingServiceButton: Bool](avplayerview/showssharingservicebutton.md)
  A Boolean value that determines whether the player view displays a sharing service button.
- [var showsFullScreenToggleButton: Bool](avplayerview/showsfullscreentogglebutton.md)
  A Boolean value that determines whether the player view displays a full-screen toggle button.
- [var showsTimecodes: Bool](avplayerview/showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var contentOverlayView: NSView?](avplayerview/contentoverlayview.md)
  A view that adds additional custom views between the video content and the controls.
- [var updatesNowPlayingInfoCenter: Bool](avplayerview/updatesnowplayinginfocenter.md)
  A Boolean value that indicates whether the player view controller updates the Now Playing info center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/actionpopupbuttonmenu)*