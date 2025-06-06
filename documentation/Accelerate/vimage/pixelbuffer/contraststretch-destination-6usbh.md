# contrastStretch(destination:)

**Framework**: Accelerate  
**Kind**: method

Stretches the histogram of an 8-bit planar pixel buffer.

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
func contrastStretch(destination: vImage.PixelBuffer<vImage.Planar8>)
```

#### Discussion

Use this function to evenly distributes a histogram’s pixel values across the full range of available pixel values.

For example, the following code stretches the contrast of an image:

```swift
let srcImage =  imageLiteral(resourceName: " ... ").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 1,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let buffer = try vImage.PixelBuffer(
    cgImage: srcImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.Planar8.self)

buffer.contrastStretch(destination: buffer)

let outputImage = buffer.makeCGImage(cgImageFormat: cgImageFormat)
```

## Parameters

- `destination`: The destination pixel buffer.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-3bo13.md)
  Stretches the histogram of a 32-bit planar pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/contraststretch(destination:)-7zo9.md)
  Stretches the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-704t6.md)
  Stretches the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/contraststretch(destination:)-2nsx9.md)
  Stretches the histogram of a multiple-plane 8-bit pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-81vq2.md)
  Stretches the histogram of a multiple-plane 32-bit pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/contraststretch(destination:)-6usbh)*