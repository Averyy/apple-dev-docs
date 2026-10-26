# init(ioSurface:plane:format:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.

**Availability**:
- macOS 10.9+ - Deprecated in 10.11

## Declaration

```swift
init(ioSurface surface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]? = nil)
```

```objc
- (instancetype) initWithIOSurface:(IOSurfaceRef) surface plane:(size_t) plane format:(CIFormat) format options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An image object initialized with the data from the IOSurface.

## Parameters

- `surface`: An IOSurface object.
- `plane`: The index of the data plane in the IOSurface object containing bitmap data for initializing the image.
- `format`: A pixel format constant. See `Pixel Formats`.
- `options`: A dictionary specifying image options. (See `Image Dictionary Keys`.)

## See Also

### Deprecated
- [init(cgLayer: CGLayer)](./init%28cglayer%29-2lgo6.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](./init%28cglayer,options%29-3p3l3.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](./init%28texture,size,flipped,colorspace%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](./init%28texture,size,flipped,options%29.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [static let textureTarget: CIImageOption](../ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](../ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
- [+ imageWithCGLayer:](./imagewithcglayer_.md)
  Creates and returns an image object from the contents supplied by a `CGLayer` object.
- [+ imageWithCGLayer:options:](./imagewithcglayer_options_.md)
  Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.
- [+ imageWithTexture:size:flipped:colorSpace:](./imagewithtexture_size_flipped_colorspace_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithTexture:size:flipped:options:](./imagewithtexture_size_flipped_options_.md)
  Creates and returns an image object initialized with data supplied by an OpenGL texture.
- [+ imageWithIOSurface:options:](./imagewithiosurface_options_.md)
  Creates, using the specified options, and returns an image from the contents of an IOSurface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(iosurface:plane:format:options:)-93isn)*