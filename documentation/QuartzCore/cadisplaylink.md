# CADisplayLink

**Framework**: Core Animation  
**Kind**: class

A timer object that allows your app to synchronize its drawing to the refresh rate of the display.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CADisplayLink
```

## Mentions

- [Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro](optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro.md)

#### Overview

Your app initializes a new display link by providing a target object and a selector to call when the system updates the screen. To synchronize your display loop with the display, your application adds it to a run loop using the [`add(to:forMode:)`](cadisplaylink/add(to:formode:).md) method.

Once you associate the display link with a run loop, the system calls the selector on the target when the screen’s contents need to update. The target can read the display link’s [`timestamp`](cadisplaylink/timestamp.md) property to retrieve the time the system displayed the previous frame. For example, an app that displays movies might use `timestamp` to calculate which video frame to display next. An app that performs its own animations might use `timestamp` to determine where and how visible objects appear in the upcoming frame.

The [`duration`](cadisplaylink/duration.md) property provides the amount of time between frames at the [`maximumFramesPerSecond`](https://developer.apple.com/documentation/UIKit/UIScreen/maximumFramesPerSecond). To calculate the actual frame duration, use [`targetTimestamp`](cadisplaylink/targettimestamp.md) - [`timestamp`](cadisplaylink/timestamp.md). You can use this value in your app to calculate the frame rate of the display, the approximate time the system displays the next frame, and to adjust the drawing behavior so that the next frame is ready in time to display.

Your app can disable notifications by setting [`isPaused`](cadisplaylink/ispaused.md) to `true`. Also, if your app can’t provide frames in the time the system provides, you may want to choose a slower frame rate. An app with a slower but consistent frame rate appears smoother to the user than an app that skips frames. You can define the number of frames per second by setting [`preferredFramesPerSecond`](cadisplaylink/preferredframespersecond.md).

When your app finishes with a display link, call [`invalidate()`](cadisplaylink/invalidate().md) to remove it from all run loops and to disassociate it from the target.

The code listing below shows how to create a display link and add it to the current run loop. The display link invokes the step function, which prints the target timestamp with each screen update.

You shouldn’t subclass [`CADisplayLink`](cadisplaylink.md).

##### Preferred and Actual Frame Rates

You control a display link’s frame rate (the number of times the system calls the selector of its target, per second) by setting [`preferredFramesPerSecond`](cadisplaylink/preferredframespersecond.md). However, the actual frames per second may differ from the preferred value you set; actual frame rates are always a factor of the maximum refresh rate of the device. For example, if your device’s maximum refresh rate is 60 frames per second (defined by [`maximumFramesPerSecond`](https://developer.apple.com/documentation/UIKit/UIScreen/maximumFramesPerSecond)), actual frame rates include 15, 20, 30, and 60 frames per second. If you set a display link’s preferred frame rate to a value higher than the maximum, the actual frame rate is the maximum.

In iOS 15, frame rate availability can change due to the system factoring in the system policy and user preference — including Low Power Mode, critical thermal state, and accessibility settings.

The system rounds, to the nearest factor, preferred frame rates that aren’t a divisor of the maximum frame rate. For example, setting a preferred frame rate to either 26 or 35 frames per second on a device with a maximum refresh rate of 60 frames per second yields an actual frame rate of 30 times per second.

The code listing below shows how to calculate the actual frame rate by dividing 1 by your display link’s [`timestamp`](cadisplaylink/timestamp.md) subtracted from its [`targetTimestamp`](cadisplaylink/targettimestamp.md).

> **Note**:  If your app needs more control over refresh rate to ensure smooth rendering of frames, use [`CAMetalDisplayLink`](cametaldisplaylink.md) and the information from [`CAMetalLayer`](cametallayer.md) instances to render frames.

 If your app needs more control over refresh rate to ensure smooth rendering of frames, use [`CAMetalDisplayLink`](cametaldisplaylink.md) and the information from [`CAMetalLayer`](cametallayer.md) instances to render frames.

## Topics

### Creating a Display Link
- [init(target: Any, selector: Selector)](cadisplaylink/init(target:selector:).md)
  Creates a display link for a target that calls its selector.
### Configuring a Display Link
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
- [var frameInterval: Int](cadisplaylink/frameinterval.md)
  The number of frames that must pass before the display link notifies the target again.
### Scheduling a Display Link to Send Notifications
- [func add(to: RunLoop, forMode: RunLoop.Mode)](cadisplaylink/add(to:formode:).md)
  Registers the display link with a run loop.
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](cadisplaylink/remove(from:formode:).md)
  Removes the display link from the run loop for the given mode.
- [func invalidate()](cadisplaylink/invalidate.md)
  Removes the display link from all run loop modes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Presenting content on a connected display](../UIKit/presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [func CACurrentMediaTime() -> CFTimeInterval](cacurrentmediatime().md)
  Returns the current absolute time, in seconds.
- [class CAMediaTimingFunction](camediatimingfunction.md)
  A function that defines the pacing of an animation as a timing curve.
- [protocol CAMediaTiming](camediatiming.md)
  Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink)*