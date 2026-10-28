# contrastStretch(destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Stretches the histogram of an 8-bit planar pixel buffer.

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
func contrastStretch(destination: vImage.PixelBuffer<vImage.Planar8>)
```

Available when `Format` is `vImage.Planar8`.

## Discussion

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

### Related Documentation
- [Enhancing image contrast with histogram manipulation](../../enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
### Contrast stretching
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](./contraststretch%28bincount,destination%29-3bo13.md)
  Stretches the histogram of a 32-bit planar pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](./contraststretch%28destination%29-7zo9.md)
  Stretches the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](./contraststretch%28bincount,destination%29-704t6.md)
  Stretches the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<Format>)](./contraststretch%28destination%29-2nsx9.md)
  Stretches the histogram of a multiple-plane 8-bit pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<Format>)](./contraststretch%28bincount,destination%29-81vq2.md)
  Stretches the histogram of a multiple-plane 32-bit pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/contraststretch(destination:)-6usbh)*