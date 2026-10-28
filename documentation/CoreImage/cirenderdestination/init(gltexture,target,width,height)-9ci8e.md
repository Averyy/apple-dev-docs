# init(glTexture:target:width:height:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a render destination based on an OpenGL texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(glTexture texture: UInt32, target: UInt32, width: Int, height: Int)
```

```objc
- (instancetype) initWithGLTexture:(unsigned int) texture target:(unsigned int) target width:(NSUInteger) width height:(NSUInteger) height;
```

## Return Value

A [`CIRenderDestination`](../cirenderdestination.md) object for rendering to a `GLTexture` supported by `GLContext`-backed [`CIContext`](../cicontext.md).

## Discussion

Rendering to a `GLTexture`-backed [`CIRenderDestination`](../cirenderdestination.md) is supported by only `GLContext`-backed [`CIContext`](../cicontext.md).

The destination’s [`colorSpace`](./colorspace.md) property will default to a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) created with [`sRGB`](../../CoreGraphics/cgcolorspace/srgb.md), [`extendedSRGB`](../../CoreGraphics/cgcolorspace/extendedsrgb.md), or [`genericGrayGamma2_2`](../../CoreGraphics/cgcolorspace/genericgraygamma2_2.md).

## Parameters

- `texture`: `GLTexture`-backed texture data.
- `target`: A value denoting the type of destination.  Use `GL_TEXTURE_2D` if your texture dimensions are a power of two, or `GL_TEXTURE_RECTANGLE_EXT` otherwise.
- `width`: Width of the texture in texels.
- `height`: Height of the texture in texels.

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
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](./init%28bitmapdata,width,height,bytesperrow,format%29.md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(gltexture:target:width:height:)-9ci8e)*