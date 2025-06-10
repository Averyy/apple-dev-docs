# NSAnimationContext

**Framework**: AppKit  
**Kind**: class

An animation context, which contains information about environment and state.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSAnimationContext
```

#### Overview

[`NSAnimationContext`](nsanimationcontext.md) is analogous to [`CATransaction`](https://developer.apple.com/documentation/QuartzCore/CATransaction) and is similar in overall concept to [`NSGraphicsContext`](nsgraphicscontext.md). Each thread maintains its own stack of nestable [`NSAnimationContext`](nsanimationcontext.md) instances, with each new instance initialized as a copy of the instance below (so, inheriting its current properties).

Multiple [`NSAnimationContext`](nsanimationcontext.md) instances can be nested, allowing a given block of code to initiate animations using its own specified duration without affecting animations initiated by surrounding code.

```objc
[NSAnimationContext beginGrouping];
// Animate enclosed operations with a duration of 1 second
[[NSAnimationContext currentContext] setDuration:1.0];
[[aView animator] setFrame:newFrame];
...
    [NSAnimationContext beginGrouping];
    // Animate alpha fades with half-second duration
    [[NSAnimationContext currentContext] setDuration:0.5];
    [[aView animator] setAlphaValue:0.75];
    [[bView animator] setAlphaValue:0.75];
    [NSAnimationContext endGrouping];
...
// Will animate with a duration of 1 second
[[bView animator] setFrame:secondFrame];
[NSAnimationContext endGrouping];
```

## Topics

### Grouping Transactions
- [class func beginGrouping()](nsanimationcontext/begingrouping.md)
  Creates a new animation grouping.
- [class func endGrouping()](nsanimationcontext/endgrouping.md)
  Ends the current animation grouping.
### Getting the Current Animation Context
- [class var current: NSAnimationContext](nsanimationcontext/current.md)
  Returns the current animation context.
### Animation Completion Handlers
- [var completionHandler: (() -> Void)?](nsanimationcontext/completionhandler.md)
  A completion Block that is called when the animations in the grouping are completed.
- [class func runAnimationGroup((NSAnimationContext) -> Void, completionHandler: (() -> Void)?)](nsanimationcontext/runanimationgroup(_:completionhandler:).md)
  Allows you to specify a completion block body after the set of animation actions whose completion will trigger the completion block.
### Modifying the Animation Duration
- [var duration: TimeInterval](nsanimationcontext/duration.md)
  The duration used by animations created as a result of setting new values for an animatable property.
- [var timingFunction: CAMediaTimingFunction?](nsanimationcontext/timingfunction.md)
  The timing function used for all animations within this animation proxy group.
### Implicit Animation
- [var allowsImplicitAnimation: Bool](nsanimationcontext/allowsimplicitanimation.md)
  Determine if animations are enabled or not for animations that occur as a result of another property change.
### Type Methods
- [class func runAnimationGroup((NSAnimationContext) -> Void)](nsanimationcontext/runanimationgroup(_:).md)
- [static func animate(Animation, changes: () -> Void, completion: (() -> Void)?)](nsanimationcontext/animate(_:changes:completion:).md)
  Animate changes to one or more views using the specified SwiftUI animation.

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

- [class NSViewAnimation](nsviewanimation.md)
  An animation of an app’s views, limited to changes in frame location and size, and to fade-in and fade-out effects.
- [protocol NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [enum NSAnimationEffect](nsanimationeffect.md)
  The type for standard system animation effects, which include both display and sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext)*