# drawableMultisample

**Framework**: GLKit  
**Kind**: property

The format of the multisampling buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var drawableMultisample: GLKViewDrawableMultisample { get set }
```

#### Discussion

The default value is [`GLKViewDrawableMultisample.multisampleNone`](glkviewdrawablemultisample/multisamplenone.md).

After your application changes the value of this property, the view recreates its framebuffer object the next time the view is drawn.

## See Also

- [var drawableColorFormat: GLKViewDrawableColorFormat](glkview/drawablecolorformat.md)
  The format of the color renderbuffer.
- [var drawableDepthFormat: GLKViewDrawableDepthFormat](glkview/drawabledepthformat.md)
  The format of the depth renderbuffer
- [var drawableStencilFormat: GLKViewDrawableStencilFormat](glkview/drawablestencilformat.md)
  The format of the stencil renderbuffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/drawablemultisample)*