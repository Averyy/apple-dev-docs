# timebase

**Framework**: AVFoundation  
**Kind**: property

The synchronizer’s rendering timebase which determines how it interprets timestamps.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var timebase: CMTimebase { get }
```

#### Discussion

The default for this property is the clock for an added [`AVSampleBufferAudioRenderer`](avsamplebufferaudiorenderer.md) object. If you haven’t added a renderer, the timebase is the system host clock.

## See Also

- [func currentTime() -> CMTime](avsamplebufferrendersynchronizer/currenttime.md)
  Returns the current time of the synchronizer.
- [var rate: Float](avsamplebufferrendersynchronizer/rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:).md)
  Sets the renderer’s time and rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:athosttime:).md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](avsamplebufferrendersynchronizer/ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/timebase)*