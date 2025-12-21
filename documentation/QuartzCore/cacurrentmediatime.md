# CACurrentMediaTime()

**Framework**: Core Animation  
**Kind**: func

Returns the current absolute time, in seconds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func CACurrentMediaTime() -> CFTimeInterval
```

## Mentions

- [Optimizing iPhone and iPad apps to support ProMotion displays](optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)

#### Return Value

A `CFTimeInterval` derived by calling `mach_absolute_time()` and converting the result to seconds.

## See Also

- [class CAMediaTimingFunction](camediatimingfunction.md)
  A function that defines the pacing of an animation as a timing curve.
- [protocol CAMediaTiming](camediatiming.md)
  Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [class CADisplayLink](cadisplaylink.md)
  A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cacurrentmediatime())*