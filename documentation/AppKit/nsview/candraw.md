# canDraw

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether drawing commands will produce any results.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var canDraw: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when drawing produces expected results. A view object can draw onscreen if it is not hidden, it is attached to a view hierarchy in a window ([`NSWindow`](nswindow.md)), and the window has a corresponding window device. A view object can also draw during printing if it is a descendant of the view being printed.

Check the value of this property before attempting to force drawing to a specific context. For example, if the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), do not call [`lockFocus()`](nsview/lockfocus().md) or do issue any drawing commands from the view. You do not need to check whether drawing can occur when calling the [`display()`](nsview/display().md) method or any of its related methods. The display methods perform appropriate checks before asking the view to draw itself.

## See Also

- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](nsview/wantsextendeddynamicrangeopenglsurface.md)
- [var acceptsTouchEvents: Bool](nsview/acceptstouchevents.md)
  A Boolean value indicating whether the view accepts touch events.
- [var wantsBestResolutionOpenGLSurface: Bool](nsview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/candraw)*