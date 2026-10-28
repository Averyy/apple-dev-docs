# controlTimebase

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (retain, nullable) CMTimebaseRef controlTimebase;
```

## Discussion

By default, this property is `nil`, which indicates the layer interprets timestamps according the host time clock (`mach_absolute_time` with the appropriate timescale conversion; this is the same as Core Animation’s [`CACurrentMediaTime()`](../../QuartzCore/cacurrentmediatime%28%29.md)). Without a control timebase, it isn’t possible to change when the layer displays frames after enqueuing them.

Setting a valid time base enables you to control the timing of frame display by setting the rate and time of the control timebase.

If you’re synchronizing video to audio, you should use a timebase whose host clock is a [`CMClock`](../../CoreMedia/cmclock.md) for the appropriate audio device to prevent drift. See [CMAudioClock](../../CoreMedia/cmaudioclock-api.md) for more information.

## See Also

### Configuring the layer
- [var isReadyForDisplay: Bool](./isreadyfordisplay.md)
  A Boolean value that indicates whether the first video frame is ready for display.
- [var videoGravity: AVLayerVideoGravity](./videogravity.md)
  A value that indicates how the layer displays video within its bounds.
- [struct AVLayerVideoGravity](../avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/controltimebase)*