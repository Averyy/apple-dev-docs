# currentTime()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the current time of the synchronizer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func currentTime() -> CMTime
```

```objc
- (CMTime) currentTime;
```

## Return Value

A [`CMTime`](../../CoreMedia/cmtime.md) object.

## See Also

### Accessing time information
- [var timebase: CMTimebase](./timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](./rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](./setrate%28_,time%29.md)
  Sets the renderer’s time and rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](./ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](./delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/currenttime())*