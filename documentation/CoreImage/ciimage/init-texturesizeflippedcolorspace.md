# init(texture:size:flipped:colorSpace:)

**Framework**: Core Image  
**Kind**: init

Initializes an image object with data supplied by an OpenGL texture.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+

## Declaration

```swift
init(texture name: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)
```

#### Return Value

The initialized image object.

#### Discussion

When you use a texture to create a [`CIImage`](ciimage.md) object, the texture must be valid in the Core Image context ([`CIContext`](cicontext.md)) that you draw the [`CIImage`](ciimage.md) object into. This means that one of the following must be true:

- The texture must be created using the `CGLContext` object that the [`CIContext`](cicontext.md) is based on.
- The context that the texture was created in must be shared with the `CGLContext` that the [`CIContext`](cicontext.md)is based on.

Note that textures do not have a retain and release mechanism. This means that your application must make sure that the texture exists for the life cycle of the image. When you no longer need the image, you can delete the texture.

Core Image ignores the texture filtering and wrap modes (`GL_TEXTURE_FILTER` and `GL_TEXTURE_WRAP`) that you set through OpenGL. The filter and wrap modes are overridden by what the CISampler object specifies when you apply a filter to the [`CIImage`](ciimage.md) object.

## Parameters

- `name`: An OpenGL texture. Because   objects are immutable, the texture  must remain unchanged for the life of the image object. See the discussion for more information.
- `size`: The dimensions of the texture.
- `flipped`:   to have Core Image flip the coordinates of the texture vertically to convert between OpenGL and Core Image coordinate systems.
- `colorSpace`: The color space that the image is defined in. This must be a Quartz color space ( ). If the   value is  , the image is not color matched. Pass   for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## See Also

- [init(cgLayer: CGLayer)](ciimage/init(cglayer:).md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/init(cglayer:options:).md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/init(texture:size:flipped:options:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/init(iosurface:plane:format:options:).md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(texture:size:flipped:colorspace:))*