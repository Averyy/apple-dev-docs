# frameInterval

**Framework**: Core Animation  
**Kind**: property

The number of frames that must pass before the display link notifies the target again.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var frameInterval: Int { get set }
```

#### Discussion

The default value is `1`, which results in the system notifying your app at the refresh rate of the display. If you set the value to a value greater than `1`, the display link notifies your app at a fraction of the native refresh rate. For example, setting the interval to `2` causes the display link to fire every other frame, providing half the frame rate.

Setting this value to less than `1` results in undefined behavior and is a programmer error.

## See Also

- [var duration: CFTimeInterval](cadisplaylink/duration.md)
  The time interval between screen refresh updates.
- [var preferredFrameRateRange: CAFrameRateRange](cadisplaylink/preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](cadisplaylink/preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var isPaused: Bool](cadisplaylink/ispaused.md)
  A Boolean value that indicates whether the system suspends the display link’s notifications to the target.
- [var timestamp: CFTimeInterval](cadisplaylink/timestamp.md)
  The time interval that represents when the last frame displayed.
- [var targetTimestamp: CFTimeInterval](cadisplaylink/targettimestamp.md)
  The time interval that represents when the next frame displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/frameinterval)*