# videoGravity

**Framework**: AVKit  
**Kind**: property

A string that specifies how the video displays within the bounds of the view controller’s view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var videoGravity: AVLayerVideoGravity { get set }
```

#### Discussion

The player view controller supports the following video gravity values: [`resizeAspect`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspect), [`resizeAspectFill`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspectFill), and [`resize`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resize).

The default value is [`resizeAspect`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspect).

## See Also

- [var showsPlaybackControls: Bool](avplayerviewcontroller/showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var contentOverlayView: UIView?](avplayerviewcontroller/contentoverlayview.md)
  A view that displays between the video content and the playback controls.
- [var videoBounds: CGRect](avplayerviewcontroller/videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](avplayerviewcontroller/showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/videogravity)*