# applyLookup(_:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a lookup table to transform an 8-bit planar image.

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
func applyLookup(_ lookupTable: [Pixel_8], destination: vImage.PixelBuffer<vImage.Planar8>)
```

#### Discussion

You can use this function to create custom response curves (that is, the value of an output pixel based on the value of the corresponding input pixel). Changing the shape of the response curve changes the brightness and contrast of an image.

The following code creates a simple lookup table that’s based on a sigmoid function. This example uses [`BNNS`](bnns.md) to create 256 `Float` values in the range `0...1` that describe a sigmoid curve. The code scales the sigmoid curve values to `0...255` and returns [`Pixel_8`](pixel_8.md) values that are suitable for use as a lookup table.

```swift
let count = 256

// The following code populates the array descriptor with sigmoid
// curve values in the range 0...1:
let sigmoidSourceValues: [Float] = vDSP.ramp(in: -10 ... 10,
                                             count: count)
let descriptor = BNNSNDArrayDescriptor.allocate(initializingFrom: sigmoidSourceValues,
                                                shape: .vector(count))
defer {
    descriptor.deallocate()
}
let activationLayer = BNNS.ActivationLayer(function: .sigmoid,
                                           input: descriptor,
                                           output: descriptor,
                                           filterParameters: nil)
try? activationLayer!.apply(batchSize: 1,
                            input: descriptor,
                            output: descriptor)

let lookup = descriptor.data!.withMemoryRebound(to: Float.self,
                                                   capacity: count) {
    // Create an `UnsafeMutableBufferPointer` from the descriptor data.
    var sigmoid = UnsafeMutableBufferPointer(start: $0,
                                             count: count)
    
    // Scale the sigmoid values from 0...1 to 0...255.
    vDSP.multiply(255.0,
                  sigmoid,
                  result: &sigmoid)
    
    // Create Pixel_8 values from the Float sigmoid values.
    return vDSP.floatingPointToInteger(sigmoid,
                                       integerType: Pixel_8.self,
                                       rounding: .towardNearestInteger)
}
```

The graph below visualizes the values in the lookup table:

![A line chart showing an s-shaped sigmoid curve.](https://docs-assets.developer.apple.com/published/e92f25bd2d14cd05d3a7e42105fc0d6d/media-4164717%402x.png)

Use the following code to apply the lookup table to a [`vImage.Planar8`](vimage/planar8.md) source buffer and write the result to a [`vImage.Planar8`](vimage/planar8.md) destination buffer:

```swift
let destinationBuffer = vImage.PixelBuffer(
    size: sourceBuffer.size,
    pixelFormat: vImage.Planar8.self)

sourceBuffer.applyLookup(lookup, destination: destinationBuffer)
```

The images below show an example grayscale source image on the left and the transformed result on the right. The operation flattens the response for very dark and very bright areas and increases the contrast in the destination image.

![Two versions of a close-up image of a fruit tree. On the left is the original grayscale image, and on the right is the transformed high-contrast image.](https://docs-assets.developer.apple.com/published/ecd3ca07235a9c8c2b75acd702d2ae39/media-4164714%402x.png)

## Parameters

- `lookupTable`: A lookup table that contains 256   ARGB values. The function discards the alpha component.
- `destination`: The destination pixel buffer.

## See Also

- [func applyLookup([Pixel_F], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applylookup(_:destination:)-14pjo.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func applyLookup([Pixel_16U], destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/applylookup(_:destination:)-5oi4o.md)
  Applies a lookup table to transform an 8-bit planar image to a 16-bit planar image.
- [func applyLookup([Pixel_8888], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applylookup(_:destination:)-3ruls.md)
  Applies a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func applyLookup([Pixel_FFFF], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applylookup(_:destination:)-1tsb5.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func applyLookup(alphaTable: [Pixel_8]?, redTable: [Pixel_8]?, greenTable: [Pixel_8]?, blueTable: [Pixel_8]?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applylookup(alphatable:redtable:greentable:bluetable:destination:).md)
  Applies a set of four lookup tables to transform an interleaved, four-channel 8-bit image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applylookup(_:destination:)-5r7bq)*