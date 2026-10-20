# timebase

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The timebase information for the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var timebase: CMTimebase? { get }
```

```objc
@property (nonatomic, readonly, nullable) CMTimebaseRef timebase;
```

#### Discussion

The system uses timebase information to synchronize playback of the current item with the host clock. You can use this property to access the timebase information, but you can’t use it to set the time or the rate of playback.

If you need to respond to changes in the effective playback rate, listen for [`kCMTimebaseNotification_EffectiveRateChanged`](../../CoreMedia/kcmtimebasenotification_effectiveratechanged.md) notifications that the player item’s [`timebase`](./timebase.md) posts. These notifications announce when the effective playback rate changes, which includes any compensation necessary for drifting behaviors of audio output hardware.

## See Also

### Accessing timing information
- [func currentTime() -> CMTime](./currenttime%28%29.md)
  Returns the current time of the item.
- [func currentDate() -> Date?](./currentdate%28%29.md)
  Returns the current time of the item as a date.
- [var duration: CMTime](./duration.md)
  The duration of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/timebase)*