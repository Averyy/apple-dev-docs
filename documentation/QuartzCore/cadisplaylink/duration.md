# duration

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The time interval between screen refresh updates.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var duration: CFTimeInterval { get }
```

```objc
@property (nonatomic, readonly) CFTimeInterval duration;
```

## Discussion

This value is in an undefined state until the system calls the target’s selector at least once.

You calculate the expected amount of time your app has to render each frame by using [`targetTimestamp`](./targettimestamp.md)-[`timestamp`](./timestamp.md). Use [`targetTimestamp`](./targettimestamp.md)-[`CACurrentMediaTime()`](../cacurrentmediatime%28%29.md) to calculate the actual amount of time.

## See Also

### Configuring a Display Link
- [var preferredFrameRateRange: CAFrameRateRange](./preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [var timestamp: CFTimeInterval](./timestamp.md)
  The time interval that represents when the last frame displayed.
- [var targetTimestamp: CFTimeInterval](./targettimestamp.md)
  The time interval that represents when the next frame displays.
- [var frameInterval: Int](./frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/duration)*