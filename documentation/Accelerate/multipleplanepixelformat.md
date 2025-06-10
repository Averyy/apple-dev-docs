# MultiplePlanePixelFormat

**Framework**: Accelerate  
**Kind**: protocol

A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.

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
protocol MultiplePlanePixelFormat : PixelFormat
```

#### Overview

Use multiple-plane pixel buffers to store image data as discrete planar buffers that represent individual channels.

For example, the following code deinterleaves an interleaved buffer and applies different gamma adjustments to different color channels. The code calls `PixelBuffer.convert(to:)` to reinterleave the image data and generates a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance of the final output.

```swift
let srcImage =  imageLiteral(resourceName: "...").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let interleaved = try vImage.PixelBuffer(
    cgImage: srcImage,
    cgImageFormat: &cgImageFormat,
    pixelFormat: vImage.Interleaved8x3.self)

let multiplane = vImage.PixelBuffer<vImage.Planar8x3>(interleavedBuffer: interleaved)

multiplane.withUnsafePixelBuffers { pixelBuffers in

    // Apply gamma to red channel.
    pixelBuffers[0].applyGamma(.nineOverElevenHalfPrecision,
                               destination: pixelBuffers[0])

    // Apply gamma to green channel.
    pixelBuffers[1].applyGamma(.fiveOverElevenHalfPrecision,
                               destination: pixelBuffers[1])
}

multiplane.convert(to: interleaved)
let outputImage = interleaved
```

## Topics

### Associated Types
- [associatedtype PlanarPixelFormat : StaticPixelFormat](multipleplanepixelformat/planarpixelformat.md)
### Type Properties
- [static var bitCountPerPlanarPixel: Int](multipleplanepixelformat/bitcountperplanarpixel.md)
- [static var planeCount: Int](multipleplanepixelformat/planecount.md)

## Relationships

### Inherits From
- [PixelFormat](pixelformat.md)
### Conforming Types
- [vImage.Planar8x2](vimage/planar8x2.md)
- [vImage.Planar8x3](vimage/planar8x3.md)
- [vImage.Planar8x4](vimage/planar8x4.md)
- [vImage.PlanarFx2](vimage/planarfx2.md)
- [vImage.PlanarFx3](vimage/planarfx3.md)
- [vImage.PlanarFx4](vimage/planarfx4.md)

## See Also

- [protocol InitializableFromCGImage](initializablefromcgimage.md)
  A pixel format that supports initialization from a Core Graphics image.
- [protocol PixelFormat](pixelformat.md)
  A pixel buffer pixel format.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/multipleplanepixelformat)*