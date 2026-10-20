# height

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The formal height of the image, in pixels.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var height: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger height;
```

## See Also

### Properties
- [var device: any MTLDevice](./device.md)
  The device on which the image will be used.
- [var width: Int](./width.md)
  The formal width of the image, in pixels.
- [var featureChannels: Int](./featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](./numberofimages.md)
  The number of images for batch processing.
- [var textureType: MTLTextureType](./texturetype.md)
  The type of the underlying texture.
- [enum MTLTextureType](../../Metal/mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The pixel format of the underlying texture.
- [enum MTLPixelFormat](../../Metal/mtlpixelformat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [var precision: Int](./precision.md)
  The number of bits of numeric precision available for each feature channel.
- [var usage: MTLTextureUsage](./usage.md)
  The intended usage of the underlying texture.
- [struct MTLTextureUsage](../../Metal/mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.
- [var pixelSize: Int](./pixelsize.md)
  The number of bytes from the first byte of one pixel to the first byte of the next pixel, in storage order. (Includes padding.)
- [var texture: any MTLTexture](./texture.md)
  The underlying texture.
- [protocol MTLTexture](../../Metal/mtltexture.md)
  A resource that holds formatted image data.
- [var label: String?](./label.md)
  A string to help identify this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/height)*