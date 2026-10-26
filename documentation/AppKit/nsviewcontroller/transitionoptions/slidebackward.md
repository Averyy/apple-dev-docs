# slideBackward

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A transition animation that reflects the user interface layout direction ([`userInterfaceLayoutDirection`](../../nsapplication/userinterfacelayoutdirection.md)) in a “backward” manner, as follows

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var slideBackward: NSViewController.TransitionOptions { get }
```

```c
NSViewControllerTransitionSlideBackward
```

#### Discussion

- For left-to-right user interface layout direction, the [`slideRight`](./slideright.md) animation option.
- For right-to-left user interface layout direction, the [`slideLeft`](./slideleft.md) animation option.

## See Also

### Constants
- [static var crossfade: NSViewController.TransitionOptions](./crossfade.md)
  A transition animation that fades the new view in and simultaneously fades the old view out. You can combine this animation option with any of the “slide” options in this enumeration.
- [static var slideUp: NSViewController.TransitionOptions](./slideup.md)
  A transition animation that slides the old view up while the new view comes into view from the bottom.  In other words, both views slide up.
- [static var slideDown: NSViewController.TransitionOptions](./slidedown.md)
  A transition animation that slides the old view down while the new view slides into view from the top. In other words, both views slide down.
- [static var slideLeft: NSViewController.TransitionOptions](./slideleft.md)
  A transition animation that slides the old view to the left while the new view slides into view from the right. In other words, both views slide to the left.
- [static var slideRight: NSViewController.TransitionOptions](./slideright.md)
  A transition animation that slides the old view to the right while the new view slides into view from the left.  In other words, both views slide to the right.
- [static var slideForward: NSViewController.TransitionOptions](./slideforward.md)
  A transition animation that reflects the user interface layout direction ([`userInterfaceLayoutDirection`](../../nsapplication/userinterfacelayoutdirection.md)) in a “forward” manner, as follows:
- [static var allowUserInteraction: NSViewController.TransitionOptions](./allowuserinteraction.md)
  A transition animation that allows user interaction during the transition.
- [NSViewControllerTransitionNone](../../nsviewcontrollertransitionoptions/nsviewcontrollertransitionnone.md)
  A transition with no animation (the default). Specifying another animation option from this enumeration overrides this option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/transitionoptions/slidebackward)*