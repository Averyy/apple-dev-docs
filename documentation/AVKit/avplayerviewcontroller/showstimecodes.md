# showsTimecodes

**Framework**: AVKit  
**Kind**: property

A Boolean value that determines whether the player view displays timecodes, if available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var showsTimecodes: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var showsPlaybackControls: Bool](avplayerviewcontroller/showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var contentOverlayView: UIView?](avplayerviewcontroller/contentoverlayview.md)
  A view that displays between the video content and the playback controls.
- [var videoGravity: AVLayerVideoGravity](avplayerviewcontroller/videogravity.md)
  A string that specifies how the video displays within the bounds of the view controller’s view.
- [var videoBounds: CGRect](avplayerviewcontroller/videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/showstimecodes)*