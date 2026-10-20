# histogramForAlpha

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

Specifies whether the histogram for the alpha channel should be computed or not.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var histogramForAlpha: ObjCBool
```

```c
BOOL histogramForAlpha;
```

## See Also

### Fields
- [var numberOfHistogramEntries: Int](./numberofhistogramentries.md)
  Specifies the number of histogram entries (*bins*) for each channel.
- [var minPixelValue: vector_float4](./minpixelvalue.md)
  Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.
- [var maxPixelValue: vector_float4](./maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo/histogramforalpha)*