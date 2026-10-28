# rate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current playback rate.

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
var rate: Float { get set }
```

```objc
@property (nonatomic, readwrite) float rate;
```

## Discussion

A value of `0.0` means playback has stopped. A value of `1.0` tells the renderer to play at the natural rate of the media. This property must be greater than or equal to `0.0`.

## See Also

### Accessing time information
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](./timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [func setRate(Float, time: CMTime)](./setrate%28_,time%29.md)
  Sets the renderer’s time and rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](./ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](./delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/rate)*