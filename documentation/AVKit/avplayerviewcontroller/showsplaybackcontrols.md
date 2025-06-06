# showsPlaybackControls

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the player view controller shows playback controls.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsPlaybackControls: Bool { get set }
```

#### Discussion

Set this property to [`false`](https://developer.apple.com/documentation/swift/false) if you don’t want the system-provided playback controls visible over your content. Hiding the playback controls can be useful in situations where you need a non-interactive video presentation, such as a video splash screen.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

> ❗ **Important**:  Don’t use this property to change the visibility of the playback controls while the player view controller is onscreen. Doing so creates or destroys user interface elements.

 Don’t use this property to change the visibility of the playback controls while the player view controller is onscreen. Doing so creates or destroys user interface elements.

## See Also

- [var contentOverlayView: UIView?](avplayerviewcontroller/contentoverlayview.md)
  A view that displays between the video content and the playback controls.
- [var videoGravity: AVLayerVideoGravity](avplayerviewcontroller/videogravity.md)
  A string that specifies how the video displays within the bounds of the view controller’s view.
- [var videoBounds: CGRect](avplayerviewcontroller/videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](avplayerviewcontroller/showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/showsplaybackcontrols)*