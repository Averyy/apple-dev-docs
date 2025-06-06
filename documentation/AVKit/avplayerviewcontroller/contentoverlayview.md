# contentOverlayView

**Framework**: AVKit  
**Kind**: property

A view that displays between the video content and the playback controls.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentOverlayView: UIView? { get }
```

#### Discussion

Use the content overlay view to add noninteractive custom views, such as a logo or watermark, between the video content and the controls.

## See Also

- [var showsPlaybackControls: Bool](avplayerviewcontroller/showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var videoGravity: AVLayerVideoGravity](avplayerviewcontroller/videogravity.md)
  A string that specifies how the video displays within the bounds of the view controller’s view.
- [var videoBounds: CGRect](avplayerviewcontroller/videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](avplayerviewcontroller/showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contentoverlayview)*