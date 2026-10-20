# drawableMultisample

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The format of the multisampling buffer.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var drawableMultisample: GLKViewDrawableMultisample { get set }
```

```objc
@property (nonatomic) GLKViewDrawableMultisample drawableMultisample;
```

#### Discussion

The default value is [`GLKViewDrawableMultisample.multisampleNone`](../glkviewdrawablemultisample/multisamplenone.md).

After your application changes the value of this property, the view recreates its framebuffer object the next time the view is drawn.

## See Also

### Configuring the Framebuffer Object
- [var drawableColorFormat: GLKViewDrawableColorFormat](./drawablecolorformat.md)
  The format of the color renderbuffer.
- [var drawableDepthFormat: GLKViewDrawableDepthFormat](./drawabledepthformat.md)
  The format of the depth renderbuffer
- [var drawableStencilFormat: GLKViewDrawableStencilFormat](./drawablestencilformat.md)
  The format of the stencil renderbuffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawablemultisample)*