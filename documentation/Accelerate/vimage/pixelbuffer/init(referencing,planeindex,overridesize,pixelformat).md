# init(referencing:planeIndex:overrideSize:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Initializes a pixel buffer by refencing the data from a single plane of a multiplane Core Video pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(referencing lockedCVPixelBuffer: CVPixelBuffer, planeIndex: Int, overrideSize: vImage.Size? = nil, pixelFormat: Format.Type = Format.self)
```

Available when `Format` conforms to `SinglePlanePixelFormat`.

## Parameters

- `lockedCVPixelBuffer`: The locked Core Video pixel buffer. Use [`CVPixelBufferLockBaseAddress(_:_:)`](../../../CoreVideo/cvpixelbufferlockbaseaddress%28_,_%29.md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](../../../CoreVideo/cvpixelbufferunlockbaseaddress%28_,_%29.md) to lock and unlock the pixel buffer.
- `planeIndex`: The index of the plane that the function references.
- `overrideSize`: An optional size that overrides the size returned by [`CVPixelBufferGetHeightOfPlane(_:_:)`](../../../CoreVideo/cvpixelbuffergetheightofplane%28_,_%29.md) and [`CVPixelBufferGetWidthOfPlane(_:_:)`](../../../CoreVideo/cvpixelbuffergetwidthofplane%28_,_%29.md). Use this parameter if you intend to pass the buffer to the any-to-any converter that requires all buffers to be the same size.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

### Creating a pixel buffer from a Core Video buffer
- [init(copying: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type) throws](./init%28copying,cvimageformat,cgimageformat,pixelformat%29.md)
  Initializes a pixel buffer by copying the data from a Core Video pixel buffer.
- [init(referencing: CVPixelBuffer, converter: vImageConverter, destinationPixelFormat: Format.Type)](./init%28referencing,converter,destinationpixelformat%29.md)
  Returns a new pixel buffer that references the specified Core Video pixel buffer and populated converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(referencing:planeindex:overridesize:pixelformat:))*