# applyMorphology(operation:destination:)

**Framework**: Accelerate  
**Kind**: method

Applies a morphology operation to an 8-bit planar pixel buffer.

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
func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)
```

## Parameters

- `operation`: An enumeration that specifies the morphology operation.
- `destination`: The destination pixel buffer.

## See Also

- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-9f8lh.md)
  Applies a morphology operation to a 32-bit planar pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_8>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-1wacj.md)
  Applies a morphology operation to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func applyMorphology(operation: vImage.MorphologyOperation<Pixel_F>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applymorphology(operation:destination:)-65xg3.md)
  Applies a morphology operation to a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [typealias StructuringElement](vimage/structuringelement.md)
  A 2D matrix that represents a morphology kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applymorphology(operation:destination:)-2bbx4)*