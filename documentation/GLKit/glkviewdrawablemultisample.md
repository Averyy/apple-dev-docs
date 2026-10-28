# GLKViewDrawableMultisample

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

The format of the multisampling buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
enum GLKViewDrawableMultisample
```

```c
enum GLKViewDrawableMultisample : GLint;
```

## Overview

Multisampling improves the quality of the output image, but may require more memory and image processing to do so. As such, you should profile your application with and without multisampling enabled, and choose a setting that provides both the image quality and performance you require.

## Topics

### Constants
- [GLKViewDrawableMultisample.multisampleNone](./glkviewdrawablemultisample/multisamplenone.md)
  Multisampling is not enabled.
- [GLKViewDrawableMultisample.multisample4X](./glkviewdrawablemultisample/multisample4x.md)
  Multisampling is enabled.
### Initializers
- [init?(rawValue: GLint)](./glkviewdrawablemultisample/init%28rawvalue%29.md)

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
- [enum GLKViewDrawableStencilFormat](./glkviewdrawablestencilformat.md)
  The format of the stencil renderbuffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewdrawablemultisample)*