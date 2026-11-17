# init(eventStatusText:eventStatusImage:eventClock:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an event status object from information you provide.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
init(eventStatusText: [String]?, eventStatusImage: UIImage?, eventClock: CPNowPlayingSportsClock?)
```

```objc
- (instancetype) initWithEventStatusText:(NSArray<NSString *> *) eventStatusText eventStatusImage:(UIImage *) eventStatusImage eventClock:(CPNowPlayingSportsClock *) eventClock;
```

## Discussion

If the `eventClock` parameter has a valid value, CarPlay displays the clock information next to the first string from the `eventStatusText` array, using the same font for both. For sports with an event clock, choose an initial string that makes sense for the event. For example, you might specify the current period of a basketball or hockey game in this string.

## Parameters

- `eventStatusText`: An array of up to three strings. The system displays the strings in the center of the Now Playing interface, stacking them vertically with the first string in the array at the top. If you specify more than three strings, the interface displays only the first three in the array. Specify `nil` if you don’t want to display any additional strings.
- `eventStatusImage`: An image to display above the event status text. Specify an image that is 30 by 30 points in size. For example, a baseball app might display an image that shows which bases have runners. Specify `nil` if you don’t want to display an image.
- `eventClock`: The current event clock information. You can specify a clock that counts up or down from an initial value. When the clock is running, CarPlay increments or decrements the clock value automatically. Specify a new clock object only when there’s a pause or resumption in gameplay, or to adjust the current clock time. Specify `nil`if the sport doesn’t use an event clock.

## See Also

### Creating a sports mode type
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus/init(eventstatustext:eventstatusimage:eventclock:))*