# apply(sources:destinations:interpolation:)

**Framework**: Accelerate  
**Kind**: method

Transforms an array of planar pixel buffers using the multidimensional lookup table.

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
func apply(sources: [vImage.PixelBuffer<vImage.PlanarF>], destinations: [vImage.PixelBuffer<vImage.PlanarF>], interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)
```

## Parameters

- `sources`: An array that contains     buffers.
- `destinations`: An array that contains     buffers.
- `interpolation`: An enumeration that specifies how the operation computes output color values that don’t have an explicit entry in the table.

## See Also

- [func apply<SrcFormat, DestFormat>(source: vImage.PixelBuffer<SrcFormat>, destination: vImage.PixelBuffer<DestFormat>, interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)](vimage/multidimensionallookuptable/apply(source:destination:interpolation:).md)
  Transforms a multiple plane pixel buffer using the multidimensional lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/apply(sources:destinations:interpolation:))*