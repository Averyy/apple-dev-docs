# init(width:height:pixelFormat:commandBuffer:mtlTextureProvider:)

**Framework**: Core Image  
**Kind**: init

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

#### Return Value

A [`CIRenderDestination`](cirenderdestination.md) object for rendering to a Metal texture.

#### Discussion

The destination’s [`colorSpace`](cirenderdestination/colorspace.md) property will default to a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) created with [`sRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/sRGB), [`extendedSRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/extendedSRGB), or [`genericGrayGamma2_2`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/genericGrayGamma2_2).

## Parameters

- `width`: Width of the [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) that will be returned by block.
- `height`: Height of the [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) that will be returned by block.
- `pixelFormat`: Pixel format of the [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) that will be returned by block.
- `commandBuffer`: An optional [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) used for rendering to the [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture).
- `block`: [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture)-rendering provider block to be called lazily when the destination is rendered to.  The block must return a texture of [`MTLTextureType`](https://developer.apple.com/documentation/Metal/MTLTextureType) of [`MTLTextureType.type2D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type2D).

## See Also

- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/init(pixelbuffer:).md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/init(iosurface:).md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](cirenderdestination/init(mtltexture:commandbuffer:).md)
  Creates a render destination based on a Metal texture.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](cirenderdestination/init(gltexture:target:width:height:).md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:).md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:))*