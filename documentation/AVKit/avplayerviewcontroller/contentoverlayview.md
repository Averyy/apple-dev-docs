# contentOverlayView

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A view that displays between the video content and the playback controls.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentOverlayView: UIView? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIView * contentOverlayView;
```

## Discussion

Use the content overlay view to add noninteractive custom views, such as a logo or watermark, between the video content and the controls.

## See Also

### Configuring presentation
- [var showsPlaybackControls: Bool](./showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var videoGravity: AVLayerVideoGravity](./videogravity.md)
  A string that specifies how the video displays within the bounds of the view controller’s view.
- [var videoBounds: CGRect](./videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](./appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contentoverlayview)*