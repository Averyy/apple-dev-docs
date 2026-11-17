# eventStatusImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image you use to convey event-related details in the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var eventStatusImage: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * eventStatusImage;
```

## Discussion

CarPlay displays this image above the strings in the `eventStatusText` property. Use the image to convey information graphically. For example, you might use the image to show the positions of runners in a baseball game. If the property is `nil`, CarPlay doesn’t display an image.

## See Also

### Getting the event status
- [var eventStatusText: [String]?](./eventstatustext.md)
  One to three strings you use to convey event-related details in the Now Playing interface.
- [var eventClock: CPNowPlayingSportsClock?](./eventclock.md)
  The clock information you provided for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus/eventstatusimage)*