# isPaused

**Framework**: Core Animation  
**Kind**: property

A Boolean value that indicates whether the system suspends the display link’s notifications to the target.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isPaused: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). If [`true`](https://developer.apple.com/documentation/swift/true), the display link doesn’t send notifications to the target.

This property is thread safe, so you can set it from a thread separate to the one in which the display link runs.

## See Also

- [var duration: CFTimeInterval](cadisplaylink/duration.md)
  The time interval between screen refresh updates.
- [var preferredFrameRateRange: CAFrameRateRange](cadisplaylink/preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](cadisplaylink/preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var timestamp: CFTimeInterval](cadisplaylink/timestamp.md)
  The time interval that represents when the last frame displayed.
- [var targetTimestamp: CFTimeInterval](cadisplaylink/targettimestamp.md)
  The time interval that represents when the next frame displays.
- [var frameInterval: Int](cadisplaylink/frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/ispaused)*