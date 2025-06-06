# setRate(_:time:atHostTime:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `rate`: A new timebase rate. This value must be greater than or equal to  .
- `time`: A new timebase time. This value must be greater than or equal to  , or  .
- `hostTime`: A new host time. This value must be greater than or equal to  , or  .

## See Also

- [func currentTime() -> CMTime](avsamplebufferrendersynchronizer/currenttime.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](avsamplebufferrendersynchronizer/timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](avsamplebufferrendersynchronizer/rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:).md)
  Sets the renderer’s time and rate.
- [class let rateDidChangeNotification: NSNotification.Name](avsamplebufferrendersynchronizer/ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:athosttime:))*