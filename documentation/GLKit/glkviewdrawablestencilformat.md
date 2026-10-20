# GLKViewDrawableStencilFormat

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

The format of the stencil renderbuffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
enum GLKViewDrawableStencilFormat
```

```c
enum GLKViewDrawableStencilFormat : GLint;
```

## Topics

### Constants
- [GLKViewDrawableStencilFormat.formatNone](./glkviewdrawablestencilformat/formatnone.md)
  The underlying framebuffer object has no stencil buffer.
- [GLKViewDrawableStencilFormat.format8](./glkviewdrawablestencilformat/format8.md)
  An 8-bit stencil entry for each pixel.
### Initializers
- [init?(rawValue: GLint)](./glkviewdrawablestencilformat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum GLKViewDrawableColorFormat](./glkviewdrawablecolorformat.md)
  The format of the color renderbuffer.
- [enum GLKViewDrawableDepthFormat](./glkviewdrawabledepthformat.md)
  The format of the depth renderbuffer.
- [enum GLKViewDrawableMultisample](./glkviewdrawablemultisample.md)
  The format of the multisampling buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewdrawablestencilformat)*