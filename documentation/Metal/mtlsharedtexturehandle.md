# MTLSharedTextureHandle

**Framework**: Metal  
**Kind**: class

A texture handle that can be shared across process address space boundaries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MTLSharedTextureHandle
```

#### Overview

`MTLSharedTextureHandle` objects may be passed between processes using XPC connections and then used to create a reference to the texture in another process. The texture in the other process needs to be created using the same [`MTLDevice`](mtldevice.md) on which the shared texture was originally created. To identify which device it was created on, you can use the [`device`](mtlsharedtexturehandle/device.md) property of the `MTLSharedTextureHandle` object.

## Topics

### Identifying the shared texture handle
- [var device: any MTLDevice](mtlsharedtexturehandle/device.md)
  The device object that created the texture.
- [var label: String?](mtlsharedtexturehandle/label.md)
  A string that identifies the texture.
### Initializers
- [init?(coder: NSCoder)](mtlsharedtexturehandle/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Understanding color-renderable pixel format sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [class MTKTextureLoader](../metalkit/mtktextureloader.md)
  An object that creates textures from existing data in common image formats.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedtexturehandle)*