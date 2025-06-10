# init(referencing:planeIndex:overrideSize:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init

Initializes a pixel buffer by refencing the data from a single plane of a multiplane Core Video pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(referencing lockedCVPixelBuffer: CVPixelBuffer, planeIndex: Int, overrideSize: vImage.Size? = nil, pixelFormat: Format.Type = Format.self)
```

## Parameters

- `lockedCVPixelBuffer`: The locked Core Video pixel buffer. Use   and   to lock and unlock the pixel buffer.
- `planeIndex`: The index of the plane that the function references.
- `overrideSize`: An optional size that overrides the size returned by   and  . Use this parameter if you intend to pass the buffer to the any-to-any converter that requires all buffers to be the same size.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

- [init(copying: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type) throws](vimage/pixelbuffer/init(copying:cvimageformat:cgimageformat:pixelformat:).md)
  Initializes a pixel buffer by copying the data from a Core Video pixel buffer.
- [init(referencing: CVPixelBuffer, converter: vImageConverter, destinationPixelFormat: Format.Type)](vimage/pixelbuffer/init(referencing:converter:destinationpixelformat:).md)
  Returns a new pixel buffer that references the specified Core Video pixel buffer and populated converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(referencing:planeindex:overridesize:pixelformat:))*