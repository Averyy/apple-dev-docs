# eventClock

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The clock information you provided for the event.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var eventClock: CPNowPlayingSportsClock? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) CPNowPlayingSportsClock * eventClock;
```

## Discussion

If you specify clock information for the event, CarPlay combines the current clock time with the first string from the [`eventStatusText`](./eventstatustext.md) property.

CarPlay increments and decrements the clock value once a second. You don’t have to update the clock information manually. However, CarPlay doesn’t make the incremented or decremented value available to your app. Initialize new [`CPNowPlayingSportsClock`](../cpnowplayingsportsclock.md) objects from actual game data when a game pauses or resumes to ensure the content synchronizes.

## See Also

### Getting the event status
- [var eventStatusText: [String]?](./eventstatustext.md)
  One to three strings you use to convey event-related details in the Now Playing interface.
- [var eventStatusImage: UIImage?](./eventstatusimage.md)
  An image you use to convey event-related details in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus/eventclock)*