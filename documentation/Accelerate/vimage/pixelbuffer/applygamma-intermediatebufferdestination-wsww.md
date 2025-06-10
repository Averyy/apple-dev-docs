# applyGamma(_:intermediateBuffer:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a gamma function to an 8-bit-per-channel, 4-channel interleaved pixel buffer.

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
func applyGamma(_ gamma: vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>? = nil, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)
```

#### Discussion

This operation applies gamma to an [`vImage.Interleaved8x4`](vimage/interleaved8x4.md) buffer by calling the underlying function [`vImageGamma_Planar8toPlanarF(_:_:_:_:)`](vimagegamma_planar8toplanarf(_:_:_:_:).md). Therefore, it requires an intermediate [`vImage.InterleavedFx4`](vimage/interleavedfx4.md) buffer. For the best performance, pass an existing [`vImage.InterleavedFx4`](vimage/interleavedfx4.md) buffer to `intermediateBuffer`, alternatively, pass ``nil`` to specify that the function creates the intermediate buffer.

For example, the following code applies a gamma of `2.0` to a one-pixel pixel buffer:

```swift
let buffer = vImage.PixelBuffer<vImage.Interleaved8x4>(
    pixelValues: [0, 64, 128, 255],
    size: vImage.Size(width: 1,
                      height: 1))

buffer.applyGamma(.fullPrecision(2),
                  destination: buffer)

// Prints "[0, 16, 64, 255]" ≅ [255 * 0², 255 * 0.25², 255 * 0.5², 255 * 1²].
print(buffer.array)
```

## Parameters

- `gamma`: An enumeration that specifies either a used-defined or constant gamma.
- `intermediateBuffer`: An optional intermediate buffer.
- `destination`: The destination pixel buffer.

## See Also

- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.PlanarF>?, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-1fif9.md)
  Applies a gamma function to an 8-bit planar pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx2>?, destination: vImage.PixelBuffer<vImage.Interleaved8x2>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-390k5.md)
  Applies a gamma function to an 8-bit-per-channel, 2-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>?, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-3yu0w.md)
  Applies a gamma function to an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applygamma(_:destination:).md)
  Applies a gamma function to a 32-bit pixel buffer.
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-wsww)*