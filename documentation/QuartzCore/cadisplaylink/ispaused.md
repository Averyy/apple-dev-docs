# isPaused

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

#### Discussion

The default value is [`false`](../../Swift/false.md). If [`true`](../../Swift/true.md), the display link doesn’t send notifications to the target.

This property is thread safe, so you can set it from a thread separate to the one in which the display link runs.

## See Also

### Configuring a Display Link
- [var duration: CFTimeInterval](./duration.md)
  The time interval between screen refresh updates.
- [var preferredFrameRateRange: CAFrameRateRange](./preferredframeraterange.md)
  A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  A frequency your app prefers for frame updates, affecting how often the system invokes your delegate’s callback.
- [var timestamp: CFTimeInterval](./timestamp.md)
  The time interval that represents when the last frame displayed.
- [var targetTimestamp: CFTimeInterval](./targettimestamp.md)
  The time interval that represents when the next frame displays.
- [var frameInterval: Int](./frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/ispaused)*