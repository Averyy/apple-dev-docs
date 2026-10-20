# timestamp

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CFTimeInterval timestamp;
```

## Mentions

- [Optimizing iPhone and iPad apps to support ProMotion displays](../optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)

#### Discussion

If you need to calculate what to display next, use [`targetTimestamp`](./targettimestamp.md) instead.

## See Also

### Configuring a Display Link
- [var duration: CFTimeInterval](./duration.md)
  The time interval between screen refresh updates.
- [var preferredFrameRateRange: CAFrameRateRange](./preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [var targetTimestamp: CFTimeInterval](./targettimestamp.md)
  The time interval that represents when the next frame displays.
- [var frameInterval: Int](./frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/timestamp)*