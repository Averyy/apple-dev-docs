# videoGravity

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A string that specifies how the video displays within the bounds of the view controller’s view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

```objc
@property (nonatomic, copy) AVLayerVideoGravity videoGravity;
```

#### Discussion

The player view controller supports the following video gravity values: [`resizeAspect`](../../AVFoundation/avlayervideogravity/resizeaspect.md), [`resizeAspectFill`](../../AVFoundation/avlayervideogravity/resizeaspectfill.md), and [`resize`](../../AVFoundation/avlayervideogravity/resize.md).

The default value is [`resizeAspect`](../../AVFoundation/avlayervideogravity/resizeaspect.md).

## See Also

### Configuring presentation
- [var showsPlaybackControls: Bool](./showsplaybackcontrols.md)
  A Boolean value that indicates whether the player view controller shows playback controls.
- [var contentOverlayView: UIView?](./contentoverlayview.md)
  A view that displays between the video content and the playback controls.
- [var videoBounds: CGRect](./videobounds.md)
  The size and position of the video image within the bounds of the view controller’s view.
- [var showsTimecodes: Bool](./showstimecodes.md)
  A Boolean value that determines whether the player view displays timecodes, if available.
- [var appliesPreferredDisplayCriteriaAutomatically: Bool](./appliespreferreddisplaycriteriaautomatically.md)
  A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/videogravity)*