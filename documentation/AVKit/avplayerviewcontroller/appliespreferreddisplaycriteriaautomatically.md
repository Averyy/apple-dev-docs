# appliesPreferredDisplayCriteriaAutomatically

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.

**Availability**:
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
var appliesPreferredDisplayCriteriaAutomatically: Bool { get set }
```

```objc
@property (nonatomic) BOOL appliesPreferredDisplayCriteriaAutomatically;
```

## Discussion

If this property value is `true`, the player uses the preferred display criteria of the video asset when playing the content in fullscreen. The display criteria is reset to the display’s default criteria when full-screen playback ends. Don’t change this value during full-screen presentation unless you’ve disposed of the player or player item.

## See Also

### Configuring presentation
- [var showsPlaybackControls: Bool](./showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var contentOverlayView: UIView?](./contentoverlayview.md)
  A view that displays between the video content and the playback controls.
- [var videoGravity: AVLayerVideoGravity](./videogravity.md)
  A string that specifies how the video displays within the bounds of the view controller’s view.
- [var videoBounds: CGRect](./videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically)*