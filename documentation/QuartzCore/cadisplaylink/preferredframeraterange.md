# preferredFrameRateRange

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A range of frequencies your app allows for frame updates, affecting how often the system invokes your delegate’s callback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var preferredFrameRateRange: CAFrameRateRange { get set }
```

```objc
@property (nonatomic) CAFrameRateRange preferredFrameRateRange;
```

## Mentions

- [Optimizing iPhone and iPad apps to support ProMotion displays](../optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)

#### Discussion

The display link makes a best attempt to invoke your app’s callback within the frequency range you set to this property. However, the system also takes into account the device’s hardware capabilities and the other tasks your game or app is running.

> ❗ **Important**:  Choose a frame rate range that your app can consistently maintain.

The system can change the available range of frame rates because it factors in system policies and a person’s preferences. For example, Low Power Mode, critical thermal state, and accessibility settings can affect the system’s frame rate.

The system typically provides a consistent frame rate by choosing one that’s a factor of the display’s maximum refresh rate. For example, a display link could invoke your callback 60 times per second for a display with a refresh rate of 60 hertz. However, the display link could invoke your callback less frequently, such as 30, 20, or 15 hertz, by setting a range with smaller values.

> **Note**:  By default, this property’s values are equal to [`default`](../caframeraterange/default.md), which is equivalent to the display’s maximum refresh rate, such as a [`UIScreen`](../../UIKit/uiscreen.md) instance’s [`maximumFramesPerSecond`](../../UIKit/uiscreen/maximumframespersecond.md) property.

For more information, see [Optimizing iPhone and iPad apps to support ProMotion displays](../optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md).

## See Also

### Configuring a Display Link
- [var duration: CFTimeInterval](./duration.md)
  The time interval between screen refresh updates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/preferredframeraterange)*