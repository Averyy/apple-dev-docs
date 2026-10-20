# init(width:height:pixelFormat:commandBuffer:mtlTextureProvider:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a render destination based on a Metal texture with specified pixel format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider block: (() -> any MTLTexture)? = nil)
```

```objc
- (instancetype) initWithWidth:(NSUInteger) width height:(NSUInteger) height pixelFormat:(MTLPixelFormat) pixelFormat commandBuffer:(id<MTLCommandBuffer>) commandBuffer mtlTextureProvider:(id<MTLTexture> (^)()) block;
```

#### Return Value

A [`CIRenderDestination`](../cirenderdestination.md) object for rendering to a Metal texture.

#### Discussion

The destination’s [`colorSpace`](./colorspace.md) property will default to a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) created with [`sRGB`](../../CoreGraphics/cgcolorspace/srgb.md), [`extendedSRGB`](../../CoreGraphics/cgcolorspace/extendedsrgb.md), or [`genericGrayGamma2_2`](../../CoreGraphics/cgcolorspace/genericgraygamma2_2.md).

## Parameters

- `width`: Width of the [`MTLTexture`](../../Metal/mtltexture.md) that will be returned by block.
- `height`: Height of the [`MTLTexture`](../../Metal/mtltexture.md) that will be returned by block.
- `pixelFormat`: Pixel format of the [`MTLTexture`](../../Metal/mtltexture.md) that will be returned by block.
- `commandBuffer`: An optional [`MTLCommandBuffer`](../../Metal/mtlcommandbuffer.md) used for rendering to the [`MTLTexture`](../../Metal/mtltexture.md).
- `block`: [`MTLTexture`](../../Metal/mtltexture.md)-rendering provider block to be called lazily when the destination is rendered to.  The block must return a texture of [`MTLTextureType`](../../Metal/mtltexturetype.md) of [`MTLTextureType.type2D`](../../Metal/mtltexturetype/type2d.md).

## See Also

### Creating a Render Destination
- [init(pixelBuffer: CVPixelBuffer)](./init%28pixelbuffer%29.md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](./init%28iosurface%29-1hfcq.md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](./init%28mtltexture,commandbuffer%29-2iu5i.md)
  Creates a render destination based on a Metal texture.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](./init%28gltexture,target,width,height%29-9ci8e.md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](./init%28bitmapdata,width,height,bytesperrow,format%29.md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:))*