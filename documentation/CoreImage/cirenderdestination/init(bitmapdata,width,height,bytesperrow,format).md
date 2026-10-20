# init(bitmapData:width:height:bytesPerRow:format:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a render destination based on a client-managed buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(bitmapData data: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)
```

```objc
- (instancetype) initWithBitmapData:(void *) data width:(NSUInteger) width height:(NSUInteger) height bytesPerRow:(NSUInteger) bytesPerRow format:(CIFormat) format;
```

#### Return Value

A [`CIRenderDestination`](../cirenderdestination.md) object for rendering to a client-managed buffer.

#### Discussion

The destination’s [`colorSpace`](../ciimage/colorspace.md) property will default to a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) created with [`sRGB`](../../CoreGraphics/cgcolorspace/srgb.md), [`extendedSRGB`](../../CoreGraphics/cgcolorspace/extendedsrgb.md), or [`genericGrayGamma2_2`](../../CoreGraphics/cgcolorspace/genericgraygamma2_2.md).

## Parameters

- `data`: Pointer to raw bits of a client-managed buffer that is at least (`bytesPerRow` * `height`) bytes in size.
- `width`: Width of the bitmap image in pixels.
- `height`: Height of the bitmap image in pixels.
- `bytesPerRow`: Number of bytes per row of data.
- `format`: Color format specifying how the colors are laid out in memory (for example, [`RGBA8`](../ciformat/rgba8.md)).

## See Also

### Creating a Render Destination
- [init(pixelBuffer: CVPixelBuffer)](./init%28pixelbuffer%29.md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](./init%28iosurface%29-1hfcq.md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](./init%28mtltexture,commandbuffer%29-2iu5i.md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](./init%28width,height,pixelformat,commandbuffer,mtltextureprovider%29.md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](./init%28gltexture,target,width,height%29-9ci8e.md)
  Creates a render destination based on an OpenGL texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:))*