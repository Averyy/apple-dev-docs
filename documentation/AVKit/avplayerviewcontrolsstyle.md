# AVPlayerViewControlsStyle

**Framework**: AVKit  
**Kind**: enum

Constants that indicate which user interface controls the view displays.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum AVPlayerViewControlsStyle
```

## Topics

### Controls Styles
- [AVPlayerViewControlsStyle.none](avplayerviewcontrolsstyle/none.md)
  The view displays no playback controls.
- [AVPlayerViewControlsStyle.inline](avplayerviewcontrolsstyle/inline.md)
  The view displays playback controls in a bar along the view’s bottom edge.
- [AVPlayerViewControlsStyle.floating](avplayerviewcontrolsstyle/floating.md)
  The view displays playback controls in a floating window over the video content.
- [AVPlayerViewControlsStyle.minimal](avplayerviewcontrolsstyle/minimal.md)
  The view presents basic controls to play and pause playback.
- [static var `default`: AVPlayerViewControlsStyle](avplayerviewcontrolsstyle/default.md)
  The view’s default controls style.
### Initializers
- [init?(rawValue: Int)](avplayerviewcontrolsstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var controlsStyle: AVPlayerViewControlsStyle](avplayerview/controlsstyle.md)
  The player view’s controls style.
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
- [var actionPopUpButtonMenu: NSMenu?](avplayerview/actionpopupbuttonmenu.md)
  An action pop-up button menu that the player view displays.
- [var updatesNowPlayingInfoCenter: Bool](avplayerview/updatesnowplayinginfocenter.md)
  A Boolean value that indicates whether the player view controller updates the Now Playing info center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrolsstyle)*