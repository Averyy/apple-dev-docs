# applyLookup(_:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.

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
func applyLookup(_ lookupTable: [Pixel_8888], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)
```

#### Discussion

You can use this function to create pseudo-color images by transforming a grayscale image to an RGB image.

The following code creates a simple lookup table with a high red response for low values, a high green response for middle values, and a high blue response for large values:

```swift
let window = vDSP.window(ofType: Float.self,
                         usingSequence: .blackman,
                         count: 256,
                         isHalfWindow: false)

let lookup: [Pixel_8888] = (0 ..< 256).map { i in
    
    let red = Pixel_8(window[ max(0, min(127 - i, 255))] * 255)
    let green = Pixel_8(window[i] * 255)
    let blue = Pixel_8(window[ max(0, min(382 - i, 255))] * 255)

    return Pixel_8888(0, red, green, blue)
}
```

The graph below visualizes the values in the lookup table:

![A line chart with three series. The dotted line represents the red values that peaks at the left and curves to zero at the middle. The solid line represents the green values that starts on the left at zero, peaks in the middle, and drops to zero at the right. The dashed line represents the blue values that starts at zero in the middle and peaks at the right.](https://docs-assets.developer.apple.com/published/3bae60a547eae2322e86938e16bd1841/media-4164668%402x.png)

Use the following code to apply the lookup table to a [`vImage.Planar8`](vimage/planar8.md) source buffer with a [`vImage.Interleaved8x3`](vimage/interleaved8x3.md) destination buffer:

```swift
let destinationBuffer = vImage.PixelBuffer (
    size: sourceBuffer.size,
    pixelFormat: vImage.Interleaved8x3.self)

sourceBuffer.applyLookup(lookup, destination: destinationBuffer)
```

The images below show an example grayscale source image on the left and the pseudo-color result on the right. The operation converts dark areas in the source to red in the destination, and light areas in the source to blue in the destination.

![Two versions of a close-up image of a fruit tree. On the left is the original grayscale image, and on the right is the transformed RGB color image.](https://docs-assets.developer.apple.com/published/c8ef99a81c21e689fbb3e60e14a83c37/media-4164667%402x.png)

## Parameters

- `lookupTable`: A lookup table that contains 256   ARGB values. The function discards the alpha component.
- `destination`: The destination pixel buffer.

## See Also

- [func applyLookup([Pixel_8], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applylookup(_:destination:)-5r7bq.md)
  Applies a lookup table to transform an 8-bit planar image.
- [func applyLookup([Pixel_F], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applylookup(_:destination:)-14pjo.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func applyLookup([Pixel_16U], destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/applylookup(_:destination:)-5oi4o.md)
  Applies a lookup table to transform an 8-bit planar image to a 16-bit planar image.
- [func applyLookup([Pixel_FFFF], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applylookup(_:destination:)-1tsb5.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func applyLookup(alphaTable: [Pixel_8]?, redTable: [Pixel_8]?, greenTable: [Pixel_8]?, blueTable: [Pixel_8]?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applylookup(alphatable:redtable:greentable:bluetable:destination:).md)
  Applies a set of four lookup tables to transform an interleaved, four-channel 8-bit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applylookup(_:destination:)-3ruls)*