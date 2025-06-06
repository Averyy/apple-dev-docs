# wantsExtendedDynamicRangeOpenGLSurface

**Framework**: AppKit  
**Kind**: property

Enables extended dynamic range values on the screen.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var wantsExtendedDynamicRangeOpenGLSurface: Bool { get set }
```

#### Discussion

If any view on the screen has this enabled, the screen which the OpenGL surface is on may have its `maximumExtendedDynamicRangeColorComponentValue` value increased. When composited by the Window Server, color values rendered by this OpenGL surface will be clamped to the screen’s `maximumExtendedDynamicRangeColorComponentValue` value rather than `1.0`.

## See Also

- [var maximumExtendedDynamicRangeColorComponentValue: CGFloat](nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)
  The current maximum color component value for the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/wantsextendeddynamicrangeopenglsurface)*