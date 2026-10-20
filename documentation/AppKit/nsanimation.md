# NSAnimation

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that manages the timing and progress of animations in the user interface.

**Availability**:
- macOS

## Declaration

```swift
class NSAnimation
```

```objc
@interface NSAnimation : NSObject
```

#### Overview

[`NSAnimation`](./nsanimation.md) also lets you link together multiple animations so that when one animation ends another one starts. It does not provide any drawing support for animation and does not directly deal with views, targets, or actions.

> **Note**:  For simple tasks requiring a timing mechanism, consider using [`Timer`](../Foundation/timer.md).

[`NSAnimation`](./nsanimation.md) objects have several characteristics, including duration, frame rate, and animation curve, which describes the relative speed of the animation over its course. You can set progress marks in an animation, each of which specifies a percentage of the animation completed; when an animation reaches a progress mark, it notifies its delegate and posts a notification to any observers. Animations execute in one of three blocking modes: blocking, non-blocking on the main thread, and non-blocking on a separate thread. The non-blocking modes permit the handling of user events while the animation is running.

##### Subclassing Notes

The usual usage pattern for `NSAnimation` is to make a subclass that overrides (at least) the [`currentProgress`](./nsanimation/currentprogress.md) property to invoke the superclass implementation and then perform whatever animation action is needed. The method implementation might use the [`currentValue`](./nsanimation/currentvalue.md) property and then use that value to update some drawing; as a consequence of getting the current value, the method [`animation(_:valueForProgress:)`](./nsanimationdelegate/animation%28_,valueforprogress%29.md) is sent to the delegate (if there is a delegate that implements the method). For more information on subclassing `NSAnimation`, see [Animation Programming Guide for Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AnimationGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003592).

## Topics

### Initializing an NSAnimation Object
- [init(duration: TimeInterval, animationCurve: NSAnimation.Curve)](./nsanimation/init%28duration,animationcurve%29.md)
  Returns an `NSAnimation` object initialized with the specified duration and animation-curve values.
### Configuring an Animation
- [var animationBlockingMode: NSAnimation.BlockingMode](./nsanimation/animationblockingmode.md)
  The blocking mode of the animation.
- [var runLoopModesForAnimating: [RunLoop.Mode]?](./nsanimation/runloopmodesforanimating.md)
  An array of strings representing the run loop modes in which the animation can run.
- [var animationCurve: NSAnimation.Curve](./nsanimation/animationcurve.md)
  The timing curve for the animation.
- [var duration: TimeInterval](./nsanimation/duration.md)
  The duration of the animation, in seconds.
- [var frameRate: Float](./nsanimation/framerate.md)
  The number of frame updates per second to generate for the animation.
### Managing the Delegate
- [var delegate: (any NSAnimationDelegate)?](./nsanimation/delegate.md)
  The animation delegate.
### Controlling and Monitoring an Animation
- [func start()](./nsanimation/start%28%29.md)
  Starts the animation represented by the receiver.
- [func stop()](./nsanimation/stop%28%29.md)
  Stops the animation represented by the receiver.
- [var isAnimating: Bool](./nsanimation/isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](./nsanimation/currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](./nsanimation/currentvalue.md)
  The current value of the animation effect, based on the current progress
### Managing Progress Marks
- [func addProgressMark(NSAnimation.Progress)](./nsanimation/addprogressmark%28_%29.md)
  Adds the progress mark to the receiver.
- [func removeProgressMark(NSAnimation.Progress)](./nsanimation/removeprogressmark%28_%29.md)
  Removes progress mark from the receiver.
- [var progressMarks: [NSNumber]](./nsanimation/progressmarks.md)
  An array of floating-point numbers representing current progress marks.
### Linking Animations Together
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./nsanimation/start%28when,reachesprogress%29.md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./nsanimation/stop%28when,reachesprogress%29.md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func clearStart()](./nsanimation/clearstart%28%29.md)
  Clears linkage to another animation that causes the receiver to start.
- [func clearStop()](./nsanimation/clearstop%28%29.md)
  Clears linkage to another animation that causes the receiver to stop.
### Constants
- [NSAnimation.Curve](./nsanimation/curve.md)
  These constants describe the curve of an animation—that is, the relative speed of an animation from start to finish.
- [NSAnimation.BlockingMode](./nsanimation/blockingmode.md)
  These constants indicate the blocking mode of an `NSAnimation` object when it is running.
- [NSAnimation.Progress](./nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [NSAnimationProgressMark Notification Key](./nsanimationprogressmark-notification-key.md)
  This constant is returned in the userInfo dictionary of the [`progressMarkNotification`](./nsanimation/progressmarknotification.md) notification.
### Notifications
- [class let progressMarkNotification: NSNotification.Name](./nsanimation/progressmarknotification.md)
  Posted when the current progress of a running animation reaches one of its progress marks.
### Initializers
- [init?(coder: NSCoder)](./nsanimation/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSViewAnimation](./nsviewanimation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom Animations
- [protocol NSAnimationDelegate](./nsanimationdelegate.md)
  A set of optional methods implemented by delegates of [`NSAnimation`](./nsanimation.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation)*