# AVPlayerView

**Framework**: AVKit  
**Kind**: class

A view that displays content from a player and presents a native user interface to control playback.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
class AVPlayerView
```

## Mentions

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)

#### Overview

The player view supports several controls styles, ranging from no controls to controls matching the look of QuickTime Player. This makes it easy for you to tailor the presentation to best match your use of the player view. Regardless of the selected controls style, the player view always supports the following standard set of keyboard shortcuts to control playback:

- The Space bar plays and pauses playback.
- The right and left arrow keys step frame-by-frame through the video.
- JKL navigation:
- The J key rewinds. Press it multiple times to cycle through rewind speeds.
- The K key stops playback.
- The L key fast-forwards. Press it multiple times to cycle through fast-forward speeds.

The player view also makes it simple to add trimming capabilities to your player. Call the view’s [`beginTrimming(completionHandler:)`](avplayerview/begintrimming(completionhandler:).md) method to present a trimming UI that matches the QuickTime Player interface.

## Topics

### Customizing the User Interface
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
- [var actionPopUpButtonMenu: NSMenu?](avplayerview/actionpopupbuttonmenu.md)
  An action pop-up button menu that the player view displays.
- [var updatesNowPlayingInfoCenter: Bool](avplayerview/updatesnowplayinginfocenter.md)
  A Boolean value that indicates whether the player view controller updates the Now Playing info center.
### Customizing the Video Presentation
- [var isReadyForDisplay: Bool](avplayerview/isreadyfordisplay.md)
  A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [var videoBounds: NSRect](avplayerview/videobounds.md)
  The current size and position of the video image that displays within the player view’s bounds.
- [var videoGravity: AVLayerVideoGravity](avplayerview/videogravity.md)
  A value that determines how the player view displays video content within its bounds.
### Configuring Frame Analysis
- [var allowsVideoFrameAnalysis: Bool](avplayerview/allowsvideoframeanalysis.md)
  A Boolean value that indicates whether to perform video frame analysis.
- [var videoFrameAnalysisTypes: AVVideoFrameAnalysisType](avplayerview/videoframeanalysistypes.md)
- [struct AVVideoFrameAnalysisType](avvideoframeanalysistype.md)
  Constants that define the types of analysis a player view controller may perform on a paused video frame.
### Configuring the Playback Speed
- [var speeds: [AVPlaybackSpeed]](avplayerview/speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [var selectedSpeed: AVPlaybackSpeed?](avplayerview/selectedspeed.md)
  The currently selected playback speed.
- [func selectSpeed(AVPlaybackSpeed)](avplayerview/selectspeed(_:).md)
  Selects a specified playback speed.
- [class AVPlaybackSpeed](avplaybackspeed.md)
  An object that represents a user-selectable playback speed in a playback user interface.
### Configuring Picture in Picture
- [var allowsPictureInPicturePlayback: Bool](avplayerview/allowspictureinpictureplayback.md)
  A Boolean value that determines whether the player view allows Picture in Picture playback.
- [var pictureInPictureDelegate: (any AVPlayerViewPictureInPictureDelegate)?](avplayerview/pictureinpicturedelegate.md)
  The Picture in Picture delegate object.
- [protocol AVPlayerViewPictureInPictureDelegate](avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.
### Magnifying Video
- [var allowsMagnification: Bool](avplayerview/allowsmagnification.md)
  A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.
- [var magnification: CGFloat](avplayerview/magnification.md)
  The factor by which the video’s view is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](avplayerview/setmagnification(_:centeredat:).md)
  Scales the video’s view by a specified factor, and centers the result on a specified point.
### Displaying the Chapter and Title
- [func flashChapterNumber(Int, chapterTitle: String?)](avplayerview/flashchapternumber(_:chaptertitle:).md)
  Displays the chapter number and title in the player view for a brief moment.
### Trimming Media
- [var canBeginTrimming: Bool](avplayerview/canbegintrimming.md)
  A Boolean value that indicates whether the player view can begin trimming.
- [func beginTrimming(completionHandler: ((AVPlayerViewTrimResult) -> Void)?)](avplayerview/begintrimming(completionhandler:).md)
  Puts the player view into trimming mode.
- [enum AVPlayerViewTrimResult](avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.
### Setting the Player Object
- [var player: AVPlayer?](avplayerview/player.md)
  The player instance that provides the media content for the view.
### Setting the Delegate Object
- [var delegate: (any AVPlayerViewDelegate)?](avplayerview/delegate.md)
  The player view’s delegate object.
- [protocol AVPlayerViewDelegate](avplayerviewdelegate.md)
  A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)
  Provide a QuickTime media-trimming experience in your macOS app.
- [class AVCaptureView](avcaptureview.md)
  A view that displays standard user interface controls for capturing media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview)*