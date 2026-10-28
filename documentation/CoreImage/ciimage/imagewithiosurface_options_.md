# imageWithIOSurface:options:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates, using the specified options, and returns an image from the contents of an IOSurface.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (CIImage *) imageWithIOSurface:(IOSurfaceRef) surface options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

An image object initialized with the data from the IOSurface.

## Parameters

- `surface`: An IOSurface object.
- `options`: A dictionary specifying image options. (See `Image Dictionary Keys`.)

## See Also

### Related Documentation
- [+ imageWithIOSurface:](./imagewithiosurface_.md)
  Creates and returns an image from the contents of an IOSurface.
### Deprecated
- [+ imageWithCGLayer:](./imagewithcglayer_.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](./imagewithcglayer_options_.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [init(cgLayer: CGLayer)](./init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](./init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [+ imageWithTexture:size:flipped:colorSpace:](./imagewithtexture_size_flipped_colorspace_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithTexture:size:flipped:options:](./imagewithtexture_size_flipped_options_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/imagewithiosurface:options:)*