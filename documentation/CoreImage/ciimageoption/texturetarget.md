# textureTarget

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

The key for an OpenGL texture target.

**Availability**:
- macOS 10.9+ - Deprecated in 10.14

> **Deprecated**: Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
static let textureTarget: CIImageOption
```

```c
extern CIImageOption const kCIImageTextureTarget;
```

#### Discussion

The value for this key must be an [`NSNumber`](../../Foundation/nsnumber.md) object containing a supported OpenGL texture target constant, either `GL_TEXTURE_2D` or `GL_TEXTURE_RECTANGLE_ARB`. You may only use this key when initializing an image using the [`init(texture:size:flipped:options:)`](../ciimage/init%28texture,size,flipped,options%29.md) method.

## See Also

### Deprecated
- [init(cgLayer: CGLayer)](../ciimage/init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](../ciimage/init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](../ciimage/init%28texture,size,flipped,colorspace%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](../ciimage/init%28texture,size,flipped,options%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](../ciimage/init%28iosurface,plane,format,options%29-93isn.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureFormat: CIImageOption](./textureformat.md)
  The key for an OpenGL texture format.
- [+ imageWithCGLayer:](../ciimage/imagewithcglayer_.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](../ciimage/imagewithcglayer_options_.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [+ imageWithTexture:size:flipped:colorSpace:](../ciimage/imagewithtexture_size_flipped_colorspace_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithTexture:size:flipped:options:](../ciimage/imagewithtexture_size_flipped_options_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](../ciimage/imagewithiosurface_options_.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/texturetarget)*