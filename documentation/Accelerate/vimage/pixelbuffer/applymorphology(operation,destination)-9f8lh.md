# applyMorphology(operation:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a morphology operation to a 32-bit planar pixel buffer.

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
func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` is `vImage.PlanarF`.

## Parameters

- `operation`: An enumeration that specifies the morphology operation.
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Adding a bokeh effect to images](../../adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
### Morphology
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)](./applymorphology%28operation,destination%29-2bbx4.md)
  Applies a morphology operation to an 8-bit planar pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)](./applymorphology%28operation,destination%29-1wacj.md)
  Applies a morphology operation to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)](./applymorphology%28operation,destination%29-65xg3.md)
  Applies a morphology operation to a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [vImage.MorphologyOperation](../morphologyoperation.md)
  Describes which morphology operation to perform.
- [typealias StructuringElement](../structuringelement.md)
  A 2D matrix that represents a morphology kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applymorphology(operation:destination:)-9f8lh)*