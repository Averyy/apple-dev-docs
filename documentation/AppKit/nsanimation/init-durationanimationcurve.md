# init(duration:animationCurve:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSAnimation` object initialized with the specified duration and animation-curve values.

**Availability**:
- macOS ?+

## Declaration

```swift
init(duration: TimeInterval, animationCurve: NSAnimation.Curve)
```

#### Return Value

An initialized `NSAnimation` instance. Returns `nil` if the object could not be initialized.

#### Discussion

You can always later change the duration of an `NSAnimation` object by changing the [`duration`](nsanimation/duration.md) property, even while the animation is running. See “Constants” for descriptions of the NSAnimationCurve constants.

## Parameters

- `duration`: The number of seconds over which the animation occurs. Specifying a negative number raises an exception.
- `animationCurve`: An `NSAnimationCurve` constant that describes the relative speed of the animation over its course; if it is zero, the default curve (`NSAnimationEaseInOut`) is used.

## See Also

- [Drawing](drawing.md)
  Draw shapes, images, and other content on the screen.
- [class NSAnimation](nsanimation.md)
  An object that manages the timing and progress of animations in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/init(duration:animationcurve:))*