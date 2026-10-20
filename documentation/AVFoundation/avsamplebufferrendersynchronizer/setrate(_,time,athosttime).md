# setRate(_:time:atHostTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the playback rate and the relationship between the current time and host time.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
func setRate(_ rate: Float, time: CMTime, atHostTime hostTime: CMTime)
```

```objc
- (void) setRate:(float) rate time:(CMTime) time atHostTime:(CMTime) hostTime;
```

## Parameters

- `rate`: A new timebase rate. This value must be greater than or equal to `0.0`.
- `time`: A new timebase time. This value must be greater than or equal to [`zero`](../../CoreMedia/cmtime/zero.md), or [`invalid`](../../CoreMedia/cmtime/invalid.md).
- `hostTime`: A new host time. This value must be greater than or equal to [`zero`](../../CoreMedia/cmtime/zero.md), or [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Accessing time information
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](./timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](./rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](./setrate%28_,time%29.md)
  Sets the renderer’s time and rate.
- [class let rateDidChangeNotification: NSNotification.Name](./ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](./delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:athosttime:))*