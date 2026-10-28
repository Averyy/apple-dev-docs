# acceptsTouchEvents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view accepts touch events.

**Availability**:
- macOS 10.6+ - Deprecated in 10.12.2

> **Deprecated**: Use [`allowedTouchTypes`](./allowedtouchtypes.md) instead.

## Declaration

```swift
var acceptsTouchEvents: Bool { get set }
```

```objc
@property BOOL acceptsTouchEvents;
```

## Discussion

A view accepts touch events when the value of this property is [`true`](../../Swift/true.md). By default, views do not accept touch events, so the default value of this property is [`false`](../../Swift/false.md). You can override this property and return a different value if you want your view to handle touch events.

## See Also

### Deprecated properties
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](./wantsextendeddynamicrangeopenglsurface.md)
- [var canDraw: Bool](./candraw.md)
  A Boolean value indicating whether drawing commands will produce any results.
- [var wantsBestResolutionOpenGLSurface: Bool](./wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/acceptstouchevents)*