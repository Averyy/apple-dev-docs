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

`MTLSharedTextureHandle` objects may be passed between processes using XPC connections and then used to create a reference to the texture in another process. The texture in the other process must be created using the same [`MTLDevice`](mtldevice.md) on which the shared texture was originally created. To identify which device it was created on, you can use the [`device`](mtlsharedtexturehandle/device.md) property of the `MTLSharedTextureHandle` object.

## Topics

### Identifying the Shared Texture Handle
- [var device: any MTLDevice](mtlsharedtexturehandle/device.md)
  The device object that created the texture.
- [var label: String?](mtlsharedtexturehandle/label.md)
  A string that identifies the texture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Understanding Color-Renderable Pixel Format Sizes](understanding-color-renderable-pixel-format-sizes.md)
  Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing Texture Data](optimizing-texture-data.md)
  Optimize a texture’s data to improve GPU or CPU access.
- [protocol MTLTexture](mtltexture.md)
  A resource that holds formatted image data.
- [enum MTLTextureCompressionType](mtltexturecompressiontype.md)
- [class MTLTextureDescriptor](mtltexturedescriptor.md)
  An object that you use to configure new Metal texture objects.
- [class MTKTextureLoader](../MetalKit/MTKTextureLoader.md)
  An object that creates textures from existing data in common image formats.
- [enum MTLPixelFormat](mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedtexturehandle)*