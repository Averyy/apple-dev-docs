# equalizeHistogram(binCount:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Equalizes the histogram of a 32-bit planar pixel buffer.

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
func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)
```

Available when `Format` is `vImage.PlanarF`.

## Discussion

Use this function to transform an image so that its histogram is more uniformly distributed across the entire range of values.

For example, the following code equalizes the histogram of an image:

```swift
let srcImage =  imageLiteral(resourceName: " ... ").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 32,
    bitsPerPixel: 32 * 1,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(rawValue: CGBitmapInfo.byteOrder32Little.rawValue |
                             CGBitmapInfo.floatComponents.rawValue |
                             CGImageAlphaInfo.none.rawValue))!

let buffer = try vImage.PixelBuffer(
    cgImage: srcImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.PlanarF.self)

buffer.equalizeHistogram(binCount: 1024,
                         destination: buffer)

let outputImage = buffer.makeCGImage(cgImageFormat: cgImageFormat)
```

## Parameters

- `binCount`: The number of histogram entries for each channel.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Enhancing image contrast with histogram manipulation](../../enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
### Equalization
- [func equalizeHistogram(destination: vImage.PixelBuffer<vImage.Planar8>)](./equalizehistogram%28destination%29-7temg.md)
  Equalizes the histogram of an 8-bit planar pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](./equalizehistogram%28destination%29-2gbmf.md)
  Equalizes the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](./equalizehistogram%28bincount,destination%29-6on8w.md)
  Equalizes the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](./equalizehistogram%28destination%29-939xn.md)
  Equalizes the histogram of a multiple-plane 8-bit pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<Format>)](./equalizehistogram%28bincount,destination%29-59li2.md)
  Equalizes the histogram of a multiple-plane 32-bit pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/equalizehistogram(bincount:destination:)-5iv0q)*