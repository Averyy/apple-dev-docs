# wantsBestResolutionOpenGLSurface

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.

**Availability**:
- macOS 10.7+ - Deprecated in 10.14

> **Deprecated**: OpenGL API deprecated; please use Metal and MetalKit.  (Define GL_SILENCE_DEPRECATION to silence these warnings.)

## Declaration

```swift
var wantsBestResolutionOpenGLSurface: Bool { get set }
```

```objc
@property BOOL wantsBestResolutionOpenGLSurface;
```

## Discussion

This property is relevant only for views bound to an [`NSOpenGLContext`](../nsopenglcontext.md) object (including, but not limited to, [`NSOpenGLView`](../nsopenglview.md) objects). Layer-backed views ignore the value in this property and configure their own backing surface at an appropriate resolution.

> ❗ **Important**:  For applications linked on macOS 10.15 or later, the default value of this property is [`true`](../../Swift/true.md). For applications linked on macOS 10.14 or earlier, the default value of this property is [`false`](../../Swift/false.md) to keep binary compatibility.

When this property is [`false`](../../Swift/false.md), the view uses a 1 pixel per point framebuffer regardless of the backing scale factor for the targeted display. When the backing scale factor is greater than `1.0`, the rendered surface contents are also magnified to the appropriate user size.

When this property is [`true`](../../Swift/true.md), AppKit has permission to allocate a higher resolution frame buffer for the view. AppKit uses the backing scale factor and the targeted display to determine whether a higher resolution buffer is appropriate, and it may change the surface resolution when the display mode changes or the view moves to a different display. The view must be able to convert between view units and pixel units when needed. For example, passing the view’s bounds unmodified to the `glViewport` function yields incorrect results at backing scale factors other than `1.0`. You can use the [`convertToBacking(_:)`](../nsview/converttobacking%28_%29-2xx45.md), [`convertToBacking(_:)`](../nsview/converttobacking%28_%29-3zors.md), and [`convertToBacking(_:)`](../nsview/converttobacking%28_%29-4ra9y.md) methods to convert coordinate values to the resolution of the backing store.

To learn more about using OpenGL in your Mac app, see [OpenGL Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987).

## See Also

### Related Documentation
- [var wantsBestResolutionOpenGLSurface: Bool](../nsview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.
### Instance Properties
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](./wantsextendeddynamicrangeopenglsurface.md)
  Enables extended dynamic range values on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/wantsbestresolutionopenglsurface)*