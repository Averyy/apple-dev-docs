# eventStatusText

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

One to three strings you use to convey event-related details in the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var eventStatusText: [String]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * eventStatusText;
```

## Discussion

If the array contains more than three strings, CarPlay displays only the first three. If the sport has an event clock, CarPlay combines the clock information with the first string in this array before displaying it. In that situation, choose an initial string that combines well with the event. For example, specify a string with the current period of a basketball or hockey game.

## See Also

### Getting the event status
- [var eventStatusImage: UIImage?](./eventstatusimage.md)
  An image you use to convey event-related details in the Now Playing interface.
- [var eventClock: CPNowPlayingSportsClock?](./eventclock.md)
  The clock information you provided for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus/eventstatustext)*