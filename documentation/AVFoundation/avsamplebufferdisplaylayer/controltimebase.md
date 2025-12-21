# controlTimebase

**Framework**: AVFoundation  
**Kind**: property

A timebase that determines how the layer interprets timestamps.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var controlTimebase: CMTimebase? { get set }
```

#### Discussion

By default, this property is `nil`, which indicates the layer interprets timestamps according the host time clock (`mach_absolute_time` with the appropriate timescale conversion; this is the same as Core Animation’s [`CACurrentMediaTime()`](https://developer.apple.com/documentation/QuartzCore/CACurrentMediaTime())). Without a control timebase, it isn’t possible to change when the layer displays frames after enqueuing them.

Setting a valid time base enables you to control the timing of frame display by setting the rate and time of the control timebase.

If you’re synchronizing video to audio, you should use a timebase whose host clock is a [`CMClock`](https://developer.apple.com/documentation/CoreMedia/CMClock) for the appropriate audio device to prevent drift. See [`CMAudioClock`](https://developer.apple.com/documentation/CoreMedia/cmaudioclock-api) for more information.

## See Also

- [var isReadyForDisplay: Bool](avsamplebufferdisplaylayer/isreadyfordisplay.md)
  A Boolean value that indicates whether the first video frame is ready for display.
- [var videoGravity: AVLayerVideoGravity](avsamplebufferdisplaylayer/videogravity.md)
  A value that indicates how the layer displays video within its bounds.
- [struct AVLayerVideoGravity](avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/controltimebase)*