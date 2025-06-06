# equalizeHistogram(binCount:destination:)

**Framework**: Accelerate  
**Kind**: method

Equalizes the histogram of a multiple-plane 32-bit pixel buffer.

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
func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

Use this function to transform an image so that its histogram is more uniformly distributed across the entire range of values.

For example, the following code equalizes the histogram of an image:

```swift
let srcImage =  imageLiteral(resourceName: " ... ").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 32,
    bitsPerPixel: 32 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: kCGBitmapByteOrder32Host.rawValue |
                             CGBitmapInfo.floatComponents.rawValue |
                             CGImageAlphaInfo.none.rawValue))!

let interleavedBuffer = try vImage.PixelBuffer(
    cgImage: srcImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.InterleavedFx3.self)

let multiplaneBuffer = vImage.PixelBuffer<vImage.PlanarFx3>(
    interleavedBuffer: interleavedBuffer)

multiplaneBuffer.equalizeHistogram(binCount: 1024,
                                   destination: multiplaneBuffer)

multiplaneBuffer.convert(to: interleavedBuffer)

let outputImage = interleavedBuffer.makeCGImage(cgImageFormat: cgImageFormat)
```

## Parameters

- `binCount`: The number of histogram entries for each channel.
- `destination`: The destination pixel buffer.

## See Also

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [func equalizeHistogram(destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/equalizehistogram(destination:)-7temg.md)
  Equalizes the histogram of an 8-bit planar pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/equalizehistogram(bincount:destination:)-5iv0q.md)
  Equalizes the histogram of a 32-bit planar pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(destination:)-2gbmf.md)
  Equalizes the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/equalizehistogram(bincount:destination:)-6on8w.md)
  Equalizes the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(destination:)-939xn.md)
  Equalizes the histogram of a multiple-plane 8-bit pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/equalizehistogram(bincount:destination:)-59li2)*