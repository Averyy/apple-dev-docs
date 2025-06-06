# NSAnimation.Progress

**Framework**: AppKit  
**Kind**: typealias

The animation progress, as a floating-point number between `0.0` and `1.0`.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias Progress = Float
```

#### Discussion

An animation progress value is returned in the `userInfo` dictionary of an [`progressMarkNotification`](nsanimation/progressmarknotification.md) notification.

## See Also

- [class NSViewAnimation](nsviewanimation.md)
  An animation of an app’s views, limited to changes in frame location and size, and to fade-in and fade-out effects.
- [protocol NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
- [class NSAnimationContext](nsanimationcontext.md)
  An animation context, which contains information about environment and state.
- [enum NSAnimationEffect](nsanimationeffect.md)
  The type for standard system animation effects, which include both display and sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/progress)*