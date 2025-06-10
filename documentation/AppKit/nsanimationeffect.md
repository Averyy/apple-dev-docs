# NSAnimationEffect

**Framework**: AppKit  
**Kind**: enum

The type for standard system animation effects, which include both display and sound.

**Availability**:
- macOS 10.3+

## Declaration

```swift
enum NSAnimationEffect
```

#### Overview

These effects are used to indicate that an item was removed from a collection, such as a toolbar, without deleting the underlying data. See [`NSShowAnimationEffect`](nsshowanimationeffect.md).

## Topics

### Constants
- [NSAnimationEffect.disappearingItemDefault](nsanimationeffect/disappearingitemdefault.md)
  The default effect.
- [NSAnimationEffect.poof](nsanimationeffect/poof.md)
  An effect showing a puff of smoke.
### Instance Methods
- [func show(centeredAt: NSPoint, size: NSSize, completionHandler: () -> Void)](nsanimationeffect/show(centeredat:size:completionhandler:).md)
### Initializers
- [init?(rawValue: UInt)](nsanimationeffect/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSViewAnimation](nsviewanimation.md)
  An animation of an app’s views, limited to changes in frame location and size, and to fade-in and fade-out effects.
- [protocol NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
- [class NSAnimationContext](nsanimationcontext.md)
  An animation context, which contains information about environment and state.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationeffect)*