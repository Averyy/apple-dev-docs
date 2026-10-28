# init(cgLayer:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes an image object  from the contents supplied by a CGLayer object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.11

> **Deprecated**: Use initWithCGImage: instead.

## Declaration

```swift
init(cgLayer layer: CGLayer)
```

```objc
- (instancetype) initWithCGLayer:(CGLayerRef) layer;
```

## Return Value

The initialized image object.

## Parameters

- `layer`: A CGLayer object. For more information see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGLayer`](../../CoreGraphics/cglayer.md).

## See Also

### Deprecated
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](./init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](./init%28texture,size,flipped,colorspace%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](./init%28texture,size,flipped,options%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](./init%28iosurface,plane,format,options%29-93isn.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](../ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](../ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
- [+ imageWithCGLayer:options:](./imagewithcglayer_options_.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [+ imageWithTexture:size:flipped:colorSpace:](./imagewithtexture_size_flipped_colorspace_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithTexture:size:flipped:options:](./imagewithtexture_size_flipped_options_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](./imagewithiosurface_options_.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.
### Related Documentation
- [+ imageWithCGLayer:](./imagewithcglayer_.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(cglayer:)-2lgo6)*