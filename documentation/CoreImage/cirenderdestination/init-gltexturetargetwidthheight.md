# init(glTexture:target:width:height:)

**Framework**: Core Image  
**Kind**: init

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

#### Return Value

A [`CIRenderDestination`](cirenderdestination.md) object for rendering to a `GLTexture` supported by `GLContext`-backed [`CIContext`](cicontext.md).

#### Discussion

Rendering to a `GLTexture`-backed [`CIRenderDestination`](cirenderdestination.md) is supported by only `GLContext`-backed [`CIContext`](cicontext.md).

The destination’s [`colorSpace`](cirenderdestination/colorspace.md) property will default to a [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) created with [`sRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/sRGB), [`extendedSRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/extendedSRGB), or [`genericGrayGamma2_2`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/genericGrayGamma2_2).

## Parameters

- `texture`:  -backed texture data.
- `target`: A value denoting the type of destination.  Use   if your texture dimensions are a power of two, or   otherwise.
- `width`: Width of the texture in texels.
- `height`: Height of the texture in texels.

## See Also

- [init(pixelBuffer: CVPixelBuffer)](cirenderdestination/init(pixelbuffer:).md)
  Creates a render destination based on a Core Video pixel buffer.
- [init(ioSurface: IOSurface)](cirenderdestination/init(iosurface:).md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](cirenderdestination/init(mtltexture:commandbuffer:).md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](cirenderdestination/init(width:height:pixelformat:commandbuffer:mtltextureprovider:).md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](cirenderdestination/init(bitmapdata:width:height:bytesperrow:format:).md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(gltexture:target:width:height:))*