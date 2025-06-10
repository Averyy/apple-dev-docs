# applyLookup(alphaTable:redTable:greenTable:blueTable:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a set of four lookup tables to transform an interleaved, four-channel 8-bit image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func applyLookup(alphaTable: [Pixel_8]?, redTable: [Pixel_8]?, greenTable: [Pixel_8]?, blueTable: [Pixel_8]?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)
```

#### Discussion

Use this function to apply individual lookup tables to each channel in an interleaved, four-channel image. Adjust the order of the tables for images that don’t use ARGB channel ordering. For example, use the `blueTable` parameter for the alpha lookup table to transform an RGBA image.

The following code creates a simple lookup table that transforms a [`vImage.Interleaved8x4`](vimage/interleaved8x4.md) pixel buffer into its negative. For example, when an input pixel has the value `255, 255, 255, 255`, the output pixel has the value `0, 0, 0, 0`. Conversely, when an input pixel has the value `0, 0, 0, 0`, the output pixel has the value `255, 255, 255, 255`.

```swift

let lookup: [Pixel_8] = (0 ..< 256).map { i in
    Pixel_8(255 - i)
}

let destinationBuffer = vImage.PixelBuffer(
    size: sourceBuffer.size,
    pixelFormat: vImage.Interleaved8x4.self)

sourceBuffer.applyLookup(alphaTable: nil,
                         redTable: lookup,
                         greenTable: lookup,
                         blueTable: lookup,
                         destination: destinationBuffer)
```

The images below show an example source image on the left and the negative result on the right.

![Two versions of a close-up image of a fruit tree. On the left is the original color image, and on the right is the transformed, negative image with its colors inverted.](https://docs-assets.developer.apple.com/published/4c40124db5d99ab6bafa4d50595bf9e8/media-4165177%402x.png)

## Parameters

- `alphaTable`: A lookup table for the alpha channel that contains 256   values. Pass   to specify that the function copies the alpha channel unchanged to the destination buffer.
- `redTable`: A lookup table for the red channel that contains 256   values. Pass   to specify that the function copies the red channel unchanged to the destination buffer.
- `greenTable`: A lookup table for the green channel that contains 256   values. Pass   to specify that the function copies the green channel unchanged to the destination buffer.
- `blueTable`: A lookup table for the blue channel that contains 256   values. Pass   to specify that the function copies the blue channel unchanged to the destination buffer.
- `destination`: The destination pixel buffer.

## See Also

- [func applyLookup([Pixel_8], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applylookup(_:destination:)-5r7bq.md)
  Applies a lookup table to transform an 8-bit planar image.
- [func applyLookup([Pixel_F], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applylookup(_:destination:)-14pjo.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func applyLookup([Pixel_16U], destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/applylookup(_:destination:)-5oi4o.md)
  Applies a lookup table to transform an 8-bit planar image to a 16-bit planar image.
- [func applyLookup([Pixel_8888], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applylookup(_:destination:)-3ruls.md)
  Applies a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func applyLookup([Pixel_FFFF], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applylookup(_:destination:)-1tsb5.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applylookup(alphatable:redtable:greentable:bluetable:destination:))*