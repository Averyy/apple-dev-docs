# delaysRateChangeUntilHasSufficientMediaData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that Indicates whether the playback should start immediately on rate change requests.

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
var delaysRateChangeUntilHasSufficientMediaData: Bool { get set }
```

```objc
@property (nonatomic) BOOL delaysRateChangeUntilHasSufficientMediaData;
```

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
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Sets the playback rate and the relationship between the current time and host time.
- [class let rateDidChangeNotification: NSNotification.Name](./ratedidchangenotification.md)
  The synchronizer’s rendering rate changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata)*