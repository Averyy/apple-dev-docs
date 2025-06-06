# setRate(_:time:)

**Framework**: AVFoundation  
**Kind**: method

Sets the renderer’s time and rate.

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
func setRate(_ rate: Float, time: CMTime)
```

#### Discussion

This method first sets the new time and then the new rendering rate. A `rate` value of `0.0` means that playback has stopped while a `rate` value of `1.0` indicates playback should be at the natural rate of the media.

## Parameters

- `rate`: The new timebase rate. This value must be greater than or equal to  .
- `time`: The new timebase time. This value must be greater than or equal to  , or  .

## See Also

- [func currentTime() -> CMTime](avsamplebufferrendersynchronizer/currenttime.md)
  Returns the current time of the synchronizer.
- [var timebase: CMTimebase](avsamplebufferrendersynchronizer/timebase.md)
  The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [var rate: Float](avsamplebufferrendersynchronizer/rate.md)
  The current playback rate.
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avsamplebufferrendersynchronizer/setrate(_:time:athosttime:).md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](avsamplebufferrendersynchronizer/ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.
- [var delaysRateChangeUntilHasSufficientMediaData: Bool](avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md)
  A Boolean value that Indicates whether the playback should start immediately on rate change requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/setrate(_:time:))*