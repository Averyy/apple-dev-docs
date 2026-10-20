# drawableColorFormat

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The format of the color renderbuffer.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var drawableColorFormat: GLKViewDrawableColorFormat { get set }
```

```objc
@property (nonatomic) GLKViewDrawableColorFormat drawableColorFormat;
```

#### Discussion

The default value is [`GLKViewDrawableColorFormat.RGBA8888`](../glkviewdrawablecolorformat/rgba8888.md).

After your application changes the value of this property, the view recreates its framebuffer object the next time the view is drawn.

## See Also

### Configuring the Framebuffer Object
- [var drawableDepthFormat: GLKViewDrawableDepthFormat](./drawabledepthformat.md)
  The format of the depth renderbuffer
- [var drawableStencilFormat: GLKViewDrawableStencilFormat](./drawablestencilformat.md)
  The format of the stencil renderbuffer.
- [var drawableMultisample: GLKViewDrawableMultisample](./drawablemultisample.md)
  The format of the multisampling buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawablecolorformat)*