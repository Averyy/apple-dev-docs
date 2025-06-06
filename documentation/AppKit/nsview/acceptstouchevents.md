# acceptsTouchEvents

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view accepts touch events.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var acceptsTouchEvents: Bool { get set }
```

#### Discussion

A view accepts touch events when the value of this property is [`true`](https://developer.apple.com/documentation/swift/true). By default, views do not accept touch events, so the default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). You can override this property and return a different value if you want your view to handle touch events.

## See Also

- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](nsview/wantsextendeddynamicrangeopenglsurface.md)
- [var canDraw: Bool](nsview/candraw.md)
  A Boolean value indicating whether drawing commands will produce any results.
- [var wantsBestResolutionOpenGLSurface: Bool](nsview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/acceptstouchevents)*