# CAMediaTiming

**Framework**: Core Animation  
**Kind**: protocol

Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol CAMediaTiming
```

#### Overview

Absolute time is defined as mach time converted to seconds. The [`CACurrentMediaTime()`](cacurrentmediatime().md) function is provided as a convenience for getting the current absolute time.

The conversion from parent time to local time has two stages:

1. Conversion to “active local time.” This includes the point at which the object appears in the parent object’s timeline and how fast it plays relative to the parent.
2. Conversion from “active local time” to “basic local time.” The timing model allows for objects to repeat their basic duration multiple times and, optionally, to play backwards before repeating.

## Topics

### Animation Start Time
- [var beginTime: CFTimeInterval](camediatiming/begintime.md)
  Specifies the begin time of the receiver in relation to its parent object, if applicable.
- [var timeOffset: CFTimeInterval](camediatiming/timeoffset.md)
  Specifies an additional time offset in active local time.
### Repeating Animations
- [var repeatCount: Float](camediatiming/repeatcount.md)
  Determines the number of times the animation will repeat.
- [var repeatDuration: CFTimeInterval](camediatiming/repeatduration.md)
  Determines how many seconds the animation will repeat for.
### Duration and Speed
- [var duration: CFTimeInterval](camediatiming/duration.md)
  Specifies the basic duration of the animation, in seconds.
- [var speed: Float](camediatiming/speed.md)
  Specifies how time is mapped to receiver’s time space from the parent time space.
### Playback Modes
- [var autoreverses: Bool](camediatiming/autoreverses.md)
  Determines if the receiver plays in the reverse upon completion.
- [var fillMode: CAMediaTimingFillMode](camediatiming/fillmode.md)
  Determines if the receiver’s presentation is frozen or removed once its active duration has completed.
### Constants
- [Fill Modes](fill-modes.md)
  These constants determine how the timed object behaves once its active duration has completed. They are used with the [`fillMode`](camediatiming/fillmode.md) property.

## Relationships

### Conforming Types
- [CAAnimation](caanimation.md)
- [CAAnimationGroup](caanimationgroup.md)
- [CABasicAnimation](cabasicanimation.md)
- [CAEAGLLayer](caeagllayer.md)
- [CAEmitterCell](caemittercell.md)
- [CAEmitterLayer](caemitterlayer.md)
- [CAGradientLayer](cagradientlayer.md)
- [CAKeyframeAnimation](cakeyframeanimation.md)
- [CALayer](calayer.md)
- [CAMetalLayer](cametallayer.md)
- [CAOpenGLLayer](caopengllayer.md)
- [CAPropertyAnimation](capropertyanimation.md)
- [CAReplicatorLayer](careplicatorlayer.md)
- [CAScrollLayer](cascrolllayer.md)
- [CAShapeLayer](cashapelayer.md)
- [CASpringAnimation](caspringanimation.md)
- [CATextLayer](catextlayer.md)
- [CATiledLayer](catiledlayer.md)
- [CATransformLayer](catransformlayer.md)
- [CATransition](catransition.md)

## See Also

- [func CACurrentMediaTime() -> CFTimeInterval](cacurrentmediatime().md)
  Returns the current absolute time, in seconds.
- [class CAMediaTimingFunction](camediatimingfunction.md)
  A function that defines the pacing of an animation as a timing curve.
- [class CADisplayLink](cadisplaylink.md)
  A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming)*