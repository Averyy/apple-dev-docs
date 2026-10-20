# animationBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s automatic animation behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var animationBehavior: NSWindow.AnimationBehavior { get set }
```

```objc
@property NSWindowAnimationBehavior animationBehavior;
```

#### Discussion

This property controls the automatic window animation behavior used when the [`orderFront(_:)`](./orderfront%28_%29.md) or [`orderOut(_:)`](./orderout%28_%29.md) methods are called. See [`NSWindow.AnimationBehavior`](./animationbehavior-swift.enum.md) for the possible values of this property.

By default, a window’s animation behavior is set to [`NSWindow.AnimationBehavior.default`](./animationbehavior-swift.enum/default.md), which causes AppKit to determine the style of animation to use automatically based on its inference of a window’s “type” from various window properties. A window’s animation behavior can be set to [`NSWindow.AnimationBehavior.none`](./animationbehavior-swift.enum/none.md) to disable AppKit’s automatic animations for the window, which may be useful if that animation interferes with an animation that your application implements.

The animation behavior can also be set to one of the other non-default [`NSWindow.AnimationBehavior`](./animationbehavior-swift.enum.md) values to override AppKit’s automatic inference of appropriate animation behavior based on the window’s apparent type, although this is not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior-swift.property)*