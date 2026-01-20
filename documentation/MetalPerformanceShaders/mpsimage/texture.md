# texture

**Framework**: Metal Performance Shaders  
**Kind**: property

The underlying texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var texture: any MTLTexture { get }
```

#### Discussion

This is a 2D texture if `numberOfImages=1` and `featureChannels<=4`. It is a 2D texture array otherwise.

To avoid the high cost of premature allocation of the underlying texture, avoid accessing this property except when strictly necessary. Calls to the `encode` methods of an [`MPSCNNKernel`](mpscnnkernel.md) object typically cause their arguments to become allocated. Likewise, [`MPSImage`](mpsimage.md) objects initialized with the [`init(texture:featureChannels:)`](mpsimage/init(texture:featurechannels:).md) method have already been allocated.

## See Also

- [var device: any MTLDevice](mpsimage/device.md)
  The device on which the image will be used.
- [var width: Int](mpsimage/width.md)
  The formal width of the image, in pixels.
- [var height: Int](mpsimage/height.md)
  The formal height of the image, in pixels.
- [var featureChannels: Int](mpsimage/featurechannels.md)
  The number of feature channels per pixel.
- [var numberOfImages: Int](mpsimage/numberofimages.md)
  The number of images for batch processing.
- [var textureType: MTLTextureType](mpsimage/texturetype.md)
  The type of the underlying texture.
- [enum MTLTextureType](../Metal/MTLTextureType.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [var pixelFormat: MTLPixelFormat](mpsimage/pixelformat.md)
  The pixel format of the underlying texture.
- [enum MTLPixelFormat](../Metal/MTLPixelFormat.md)
  The data formats that describe the organization and characteristics of individual pixels in a texture.
- [var precision: Int](mpsimage/precision.md)
  The number of bits of numeric precision available for each feature channel.
- [var usage: MTLTextureUsage](mpsimage/usage.md)
  The intended usage of the underlying texture.
- [struct MTLTextureUsage](../Metal/MTLTextureUsage.md)
  An enumeration for the various options that determine how you can use a texture.
- [var pixelSize: Int](mpsimage/pixelsize.md)
  The number of bytes from the first byte of one pixel to the first byte of the next pixel, in storage order. (Includes padding.)
- [protocol MTLTexture](../Metal/MTLTexture.md)
  A resource that holds formatted image data.
- [var label: String?](mpsimage/label.md)
  A string to help identify this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/texture)*