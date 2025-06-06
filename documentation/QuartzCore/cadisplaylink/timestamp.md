# timestamp

**Framework**: Core Animation  
**Kind**: property

The time interval that represents when the last frame displayed.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timestamp: CFTimeInterval { get }
```

## Mentions

- [Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro](optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro.md)

#### Discussion

If you need to calculate what to display next, use [`targetTimestamp`](cadisplaylink/targettimestamp.md) instead.

## See Also

- [var duration: CFTimeInterval](cadisplaylink/duration.md)
  The time interval between screen refresh updates.
- [var preferredFrameRateRange: CAFrameRateRange](cadisplaylink/preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](cadisplaylink/preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var isPaused: Bool](cadisplaylink/ispaused.md)
  A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [var targetTimestamp: CFTimeInterval](cadisplaylink/targettimestamp.md)
  The time interval that represents when the next frame displays.
- [var frameInterval: Int](cadisplaylink/frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/timestamp)*