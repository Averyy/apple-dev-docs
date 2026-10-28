# frameInterval

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The number of frames that must pass before the display link notifies the target again.

**Availability**:
- iOS 3.1+ - Deprecated in 10.0
- iPadOS 3.1+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`preferredFramesPerSecond`](./preferredframespersecond.md) instead.

## Declaration

```swift
var frameInterval: Int { get set }
```

```objc
@property (nonatomic) NSInteger frameInterval;
```

## Discussion

The default value is `1`, which results in the system notifying your app at the refresh rate of the display. If you set the value to a value greater than `1`, the display link notifies your app at a fraction of the native refresh rate. For example, setting the interval to `2` causes the display link to fire every other frame, providing half the frame rate.

Setting this value to less than `1` results in undefined behavior and is a programmer error.

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
- [var timestamp: CFTimeInterval](./timestamp.md)
  The time interval that represents when the last frame displayed.
- [var targetTimestamp: CFTimeInterval](./targettimestamp.md)
  The time interval that represents when the next frame displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/frameinterval)*