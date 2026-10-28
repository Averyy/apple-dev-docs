# init(mtlTexture:commandBuffer:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a render destination based on a Metal texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(mtlTexture texture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)
```

```objc
- (instancetype) initWithMTLTexture:(id<MTLTexture>) texture commandBuffer:(id<MTLCommandBuffer>) commandBuffer;
```

## Return Value

A [`CIRenderDestination`](../cirenderdestination.md) object for rendering to a Metal buffer.

## Discussion

Rendering to a [`MTLTexture`](../../Metal/mtltexture.md)-backed [`CIRenderDestination`](../cirenderdestination.md) is supported by only [`MTLTexture`](../../Metal/mtltexture.md)-backed [`CIContext`](../cicontext.md) objects.  The texture must have [`MTLTextureType`](../../Metal/mtltexturetype.md) of [`MTLTextureType.type2D`](../../Metal/mtltexturetype/type2d.md).

The destination’s [`colorSpace`](./colorspace.md) property will default to a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) created with [`sRGB`](../../CoreGraphics/cgcolorspace/srgb.md), [`extendedSRGB`](../../CoreGraphics/cgcolorspace/extendedsrgb.md), or [`genericGrayGamma2_2`](../../CoreGraphics/cgcolorspace/genericgraygamma2_2.md).

## Parameters

- `texture`: The [`MTLTexture`](../../Metal/mtltexture.md) object for rendering with [`MTLTextureType`](../../Metal/mtltexturetype.md) of [`MTLTextureType.type2D`](../../Metal/mtltexturetype/type2d.md).
- `commandBuffer`: An optional [`MTLCommandBuffer`](../../Metal/mtlcommandbuffer.md) to use for rendering to the [`MTLTexture`](../../Metal/mtltexture.md) destination.

## See Also

### Creating a Render Destination
- [init(pixelBuffer: CVPixelBuffer)](./init%28pixelbuffer%29.md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](./init%28iosurface%29-1hfcq.md)
  Creates a render destination based on an `IOSurface` object.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](./init%28width,height,pixelformat,commandbuffer,mtltextureprovider%29.md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](./init%28gltexture,target,width,height%29-9ci8e.md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](./init%28bitmapdata,width,height,bytesperrow,format%29.md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(mtltexture:commandbuffer:)-2iu5i)*