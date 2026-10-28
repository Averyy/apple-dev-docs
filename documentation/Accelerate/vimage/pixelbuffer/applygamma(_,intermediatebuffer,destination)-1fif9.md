# applyGamma(_:intermediateBuffer:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a gamma function to an 8-bit planar pixel buffer.

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
func applyGamma(_ gamma: vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.PlanarF>? = nil, destination: vImage.PixelBuffer<vImage.Planar8>)
```

Available when `Format` is `vImage.Planar8`.

## Discussion

This operation applies gamma to an [`vImage.Planar8`](../planar8.md) buffer by calling the underlying function [`vImageGamma_Planar8toPlanarF(_:_:_:_:)`](../../vimagegamma_planar8toplanarf%28_,_,_,_%29.md). Therefore, it requires an intermediate [`vImage.PlanarF`](../planarf.md) buffer. For the best performance, pass an existing [`vImage.PlanarF`](../planarf.md) buffer to `intermediateBuffer`, alternatively, pass ``nil`` to specify that the function creates the intermediate buffer.

For example, the following code applies a gamma of `2.0` to a one-pixel pixel buffer:

```swift
let buffer = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [128],
    size: vImage.Size(width: 1,
                      height: 1))

buffer.applyGamma(.fullPrecision(2),
                  destination: buffer)

// Prints "[64]" ≅ [255 * 0.5²].
print(buffer.array)
```

## Parameters

- `gamma`: An enumeration that specifies either a used-defined or constant gamma.
- `intermediateBuffer`: An optional intermediate buffer.
- `destination`: The destination pixel buffer.

## See Also

### Applying gamma
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx2>?, destination: vImage.PixelBuffer<vImage.Interleaved8x2>)](./applygamma%28_,intermediatebuffer,destination%29-390k5.md)
  Applies a gamma function to an 8-bit-per-channel, 2-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>?, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](./applygamma%28_,intermediatebuffer,destination%29-3yu0w.md)
  Applies a gamma function to an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](./applygamma%28_,intermediatebuffer,destination%29-wsww.md)
  Applies a gamma function to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, destination: vImage.PixelBuffer<Format>)](./applygamma%28_,destination%29.md)
  Applies a gamma function to a 32-bit pixel buffer.
- [vImage.Gamma](../gamma.md)
  Describes either a used-defined or constant gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-1fif9)*