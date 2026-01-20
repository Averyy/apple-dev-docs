# numberOfHistogramEntries

**Framework**: Metal Performance Shaders  
**Kind**: property

Specifies the number of histogram entries () for each channel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var numberOfHistogramEntries: Int
```

#### Discussion

This value must be both a power of 2 and a minimum of 256 bins.

For example, if you want 256 histogram bins then this value must be set to 256. The value stored in each histogram bin is a 32-bit unsigned integer. The size of the histogram buffer in which these bins will be stored should be more than or equal to:

`number of histogram entries * sizeof(uint32_t) * number of channels in the image`

## See Also

- [var histogramForAlpha: ObjCBool](mpsimagehistograminfo/histogramforalpha.md)
  Specifies whether the histogram for the alpha channel should be computed or not.
- [var minPixelValue: vector_float4](mpsimagehistograminfo/minpixelvalue.md)
  Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.
- [var maxPixelValue: vector_float4](mpsimagehistograminfo/maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo/numberofhistogramentries)*