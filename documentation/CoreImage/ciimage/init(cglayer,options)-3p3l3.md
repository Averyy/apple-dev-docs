# init(cgLayer:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.

**Availability**:
- macOS 10.4+ - Deprecated in 10.11

> **Deprecated**: Use initWithCGImage:options instead.

## Declaration

```swift
init(cgLayer layer: CGLayer, options: [CIImageOption : Any]? = nil)
```

```objc
- (instancetype) initWithCGLayer:(CGLayerRef) layer options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

The initialized image object.

## Parameters

- `layer`: A CGLayer object. For more information see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGLayer`](../../CoreGraphics/cglayer.md).
- `options`: A dictionary specifying image options. (See `Image Dictionary Keys`.)

## See Also

### Deprecated
- [init(cgLayer: CGLayer)](./init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(cglayer:options:)-3p3l3)*