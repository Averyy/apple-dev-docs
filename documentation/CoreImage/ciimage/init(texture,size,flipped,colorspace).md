# init(texture:size:flipped:colorSpace:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes an image object with data supplied by an OpenGL texture.

**Availability**:
- iOS 6.0+ - Deprecated in 12.0
- iPadOS 6.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.14
- tvOS - Deprecated in 12.0

> **Deprecated**: Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init(texture name: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)
```

```objc
- (instancetype) initWithTexture:(unsigned int) name size:(CGSize) size flipped:(BOOL) flipped colorSpace:(CGColorSpaceRef) colorSpace;
```

#### Return Value

The initialized image object.

#### Discussion

When you use a texture to create a [`CIImage`](../ciimage.md) object, the texture must be valid in the Core Image context ([`CIContext`](../cicontext.md)) that you draw the [`CIImage`](../ciimage.md) object into. This means that one of the following must be true:

- The texture must be created using the `CGLContext` object that the [`CIContext`](../cicontext.md) is based on.
- The context that the texture was created in must be shared with the `CGLContext` that the [`CIContext`](../cicontext.md)is based on.

Note that textures do not have a retain and release mechanism. This means that your application must make sure that the texture exists for the life cycle of the image. When you no longer need the image, you can delete the texture.

Core Image ignores the texture filtering and wrap modes (`GL_TEXTURE_FILTER` and `GL_TEXTURE_WRAP`) that you set through OpenGL. The filter and wrap modes are overridden by what the CISampler object specifies when you apply a filter to the [`CIImage`](../ciimage.md) object.

## Parameters

- `name`: An OpenGL texture. Because [`CIImage`](../ciimage.md) objects are immutable, the texture  must remain unchanged for the life of the image object. See the discussion for more information.
- `size`: The dimensions of the texture.
- `flipped`: `true` to have Core Image flip the coordinates of the texture vertically to convert between OpenGL and Core Image coordinate systems.
- `colorSpace`: The color space that the image is defined in. This must be a Quartz color space ([`CGColorSpace`](../../CoreGraphics/cgcolorspace.md)). If the `colorSpace` value is `nil`, the image is not color matched. Pass `nil` for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## See Also

### Deprecated
- [init(cgLayer: CGLayer)](./init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](./init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](./init%28texture,size,flipped,options%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](./init%28iosurface,plane,format,options%29-93isn.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](../ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](../ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
- [+ imageWithCGLayer:](./imagewithcglayer_.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](./imagewithcglayer_options_.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [+ imageWithTexture:size:flipped:options:](./imagewithtexture_size_flipped_options_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](./imagewithiosurface_options_.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.
### Related Documentation
- [+ imageWithTexture:size:flipped:colorSpace:](./imagewithtexture_size_flipped_colorspace_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(texture:size:flipped:colorspace:))*