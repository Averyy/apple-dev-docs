# apply(sources:destinations:interpolation:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Transforms an array of planar pixel buffers using the multidimensional lookup table.

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
func apply(sources: [vImage.PixelBuffer<vImage.PlanarF>], destinations: [vImage.PixelBuffer<vImage.PlanarF>], interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)
```

## Parameters

- `sources`: An array that contains [`sourceChannelCount`](./sourcechannelcount.md) [`vImage.PlanarF`](../planarf.md) buffers.
- `destinations`: An array that contains [`destinationChannelCount`](./destinationchannelcount.md) [`vImage.PlanarF`](../planarf.md) buffers.
- `interpolation`: An enumeration that specifies how the operation computes output color values that don’t have an explicit entry in the table.

## See Also

### Instance Methods
- [func apply<SrcFormat, DestFormat>(source: vImage.PixelBuffer<SrcFormat>, destination: vImage.PixelBuffer<DestFormat>, interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)](./apply%28source,destination,interpolation%29.md)
  Transforms a multiple plane pixel buffer using the multidimensional lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/apply(sources:destinations:interpolation:))*