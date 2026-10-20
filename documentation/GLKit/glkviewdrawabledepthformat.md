# GLKViewDrawableDepthFormat

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

The format of the depth renderbuffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
enum GLKViewDrawableDepthFormat
```

```c
enum GLKViewDrawableDepthFormat : GLint;
```

## Topics

### Constants
- [GLKViewDrawableDepthFormat.formatNone](./glkviewdrawabledepthformat/formatnone.md)
  The underlying framebuffer object has no depth buffer.
- [GLKViewDrawableDepthFormat.format16](./glkviewdrawabledepthformat/format16.md)
  A 16-bit depth entry for each pixel.
- [GLKViewDrawableDepthFormat.format24](./glkviewdrawabledepthformat/format24.md)
  A 24-bit depth entry for each pixel.
### Initializers
- [init?(rawValue: GLint)](./glkviewdrawabledepthformat/init%28rawvalue%29.md)

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
- [enum GLKViewDrawableStencilFormat](./glkviewdrawablestencilformat.md)
  The format of the stencil renderbuffer.
- [enum GLKViewDrawableMultisample](./glkviewdrawablemultisample.md)
  The format of the multisampling buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewdrawabledepthformat)*