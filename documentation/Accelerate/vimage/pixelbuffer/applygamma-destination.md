# applyGamma(_:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a gamma function to a 32-bit pixel buffer.

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
func applyGamma(_ gamma: vImage.Gamma, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

For example, the following code applies a gamma of `2.0` to a one-pixel pixel buffer:

```swift
let buffer = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.5],
    size: vImage.Size(width: 1,
                      height: 1))

buffer.applyGamma(.fullPrecision(2),
                  destination: buffer)

// Prints "[0.25]" = [0.5²].
print(buffer.array)
```

## Parameters

- `gamma`: An enumeration that specifies either a used-defined or constant gamma.
- `destination`: The destination pixel buffer.

## See Also

- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.PlanarF>?, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-1fif9.md)
  Applies a gamma function to an 8-bit planar pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx2>?, destination: vImage.PixelBuffer<vImage.Interleaved8x2>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-390k5.md)
  Applies a gamma function to an 8-bit-per-channel, 2-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>?, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-3yu0w.md)
  Applies a gamma function to an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-wsww.md)
  Applies a gamma function to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applygamma(_:destination:))*