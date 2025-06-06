# animationBehavior

**Framework**: AppKit  
**Kind**: property

The window’s automatic animation behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var animationBehavior: NSWindow.AnimationBehavior { get set }
```

#### Discussion

This property controls the automatic window animation behavior used when the [`orderFront(_:)`](nswindow/orderfront(_:).md) or [`orderOut(_:)`](nswindow/orderout(_:).md) methods are called. See [`NSWindow.AnimationBehavior`](nswindow/animationbehavior-swift.enum.md) for the possible values of this property.

By default, a window’s animation behavior is set to [`NSWindow.AnimationBehavior.default`](nswindow/animationbehavior-swift.enum/default.md), which causes AppKit to determine the style of animation to use automatically based on its inference of a window’s “type” from various window properties. A window’s animation behavior can be set to [`NSWindow.AnimationBehavior.none`](nswindow/animationbehavior-swift.enum/none.md) to disable AppKit’s automatic animations for the window, which may be useful if that animation interferes with an animation that your application implements.

The animation behavior can also be set to one of the other non-default [`NSWindow.AnimationBehavior`](nswindow/animationbehavior-swift.enum.md) values to override AppKit’s automatic inference of appropriate animation behavior based on the window’s apparent type, although this is not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/animationbehavior-swift.property)*