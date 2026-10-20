# drawableDepthFormat

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The format of the depth renderbuffer

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var drawableDepthFormat: GLKViewDrawableDepthFormat { get set }
```

```objc
@property (nonatomic) GLKViewDrawableDepthFormat drawableDepthFormat;
```

#### Discussion

The default value is [`GLKViewDrawableDepthFormat.formatNone`](../glkviewdrawabledepthformat/formatnone.md).

After your application changes the value of this property, the view recreates its framebuffer object the next time the view is drawn.

## See Also

### Configuring the Framebuffer Object
- [var drawableColorFormat: GLKViewDrawableColorFormat](./drawablecolorformat.md)
  The format of the color renderbuffer.
- [var drawableStencilFormat: GLKViewDrawableStencilFormat](./drawablestencilformat.md)
  The format of the stencil renderbuffer.
- [var drawableMultisample: GLKViewDrawableMultisample](./drawablemultisample.md)
  The format of the multisampling buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawabledepthformat)*