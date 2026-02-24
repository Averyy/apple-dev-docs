# init(cgLayer:options:)

**Framework**: Core Image  
**Kind**: init

Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init(cgLayer layer: CGLayer, options: [CIImageOption : Any]? = nil)
```

#### Return Value

The initialized image object.

## Parameters

- `layer`: A CGLayer object. For more information see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGLayer`](https://developer.apple.com/documentation/CoreGraphics/CGLayer).
- `options`: A dictionary specifying image options. (See `Image Dictionary Keys`.)

## See Also

- [init(cgLayer: CGLayer)](ciimage/init(cglayer:).md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/init(texture:size:flipped:colorspace:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/init(texture:size:flipped:options:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/init(iosurface:plane:format:options:).md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(cglayer:options:))*