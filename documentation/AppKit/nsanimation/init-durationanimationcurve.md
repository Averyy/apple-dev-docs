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
- `animationCurve`: An   constant that describes the relative speed of the animation over its course; if it is zero, the default curve ( ) is used.

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [Animation Programming Guide for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AnimationGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003592)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/init(duration:animationcurve:))*