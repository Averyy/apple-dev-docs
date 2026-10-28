# init(pixelBuffer:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a render destination based on a Core Video pixel buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(pixelBuffer: CVPixelBuffer)
```

```objc
- (instancetype) initWithPixelBuffer:(CVPixelBufferRef) pixelBuffer;
```

## Return Value

A [`CIRenderDestination`](../cirenderdestination.md) object for rendering to a [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md).

## Discussion

The destination’s [`colorSpace`](./colorspace.md) property will default to a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) created by querying the [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) object’s attributes.

## Parameters

- `pixelBuffer`: The [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) render target.

## See Also

### Creating a Render Destination
- [init(ioSurface: IOSurface)](./init%28iosurface%29-1hfcq.md)
  Creates a render destination based on an `IOSurface` object.
- [init(mtlTexture: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?)](./init%28mtltexture,commandbuffer%29-2iu5i.md)
  Creates a render destination based on a Metal texture.
- [init(width: Int, height: Int, pixelFormat: MTLPixelFormat, commandBuffer: (any MTLCommandBuffer)?, mtlTextureProvider: (() -> any MTLTexture)?)](./init%28width,height,pixelformat,commandbuffer,mtltextureprovider%29.md)
  Creates a render destination based on a Metal texture with specified pixel format.
- [init(glTexture: UInt32, target: UInt32, width: Int, height: Int)](./init%28gltexture,target,width,height%29-9ci8e.md)
  Creates a render destination based on an OpenGL texture.
- [init(bitmapData: UnsafeMutableRawPointer, width: Int, height: Int, bytesPerRow: Int, format: CIFormat)](./init%28bitmapdata,width,height,bytesperrow,format%29.md)
  Creates a render destination based on a client-managed buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/init(pixelbuffer:))*