# apply(source:destination:interpolation:)

**Framework**: Accelerate  
**Kind**: method

Transforms a multiple plane pixel buffer using the multidimensional lookup table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func apply<SrcFormat, DestFormat>(source: vImage.PixelBuffer<SrcFormat>, destination: vImage.PixelBuffer<DestFormat>, interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod) where SrcFormat : MultiplePlanePixelFormat, DestFormat : MultiplePlanePixelFormat, SrcFormat.ComponentType == Float, DestFormat.ComponentType == Float
```

## Parameters

- `source`: A multiple plane [`Pixel_F`](pixel_f.md) pixel buffer that contains [`sourceChannelCount`](vimage/multidimensionallookuptable/sourcechannelcount.md) planes.
- `destination`: A multiple plane [`Pixel_F`](pixel_f.md) pixel buffer that contains [`destinationChannelCount`](vimage/multidimensionallookuptable/destinationchannelcount.md) planes.
- `interpolation`: An enumeration that specifies how the operation computes output color values that don’t have an explicit entry in the table.

## See Also

- [func apply(sources: [vImage.PixelBuffer<vImage.PlanarF>], destinations: [vImage.PixelBuffer<vImage.PlanarF>], interpolation: vImage.MultidimensionalLookupTable.InterpolationMethod)](vimage/multidimensionallookuptable/apply(sources:destinations:interpolation:).md)
  Transforms an array of planar pixel buffers using the multidimensional lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/multidimensionallookuptable/apply(source:destination:interpolation:))*