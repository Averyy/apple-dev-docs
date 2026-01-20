# zeroHistogram

**Framework**: Metal Performance Shaders  
**Kind**: property

Determines whether to zero-initialize the histogram results.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var zeroHistogram: Bool { get set }
```

#### Discussion

Determines whether the memory region in which the histogram results are to be written in the histogram buffer are to be zero-initialized or not.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var clipRectSource: MTLRegion](mpsimagehistogram/cliprectsource.md)
  The source rectangle to use when reading data.
- [var histogramInfo: MPSImageHistogramInfo](mpsimagehistogram/histograminfo.md)
  A structure describing the histogram content.
- [var minPixelThresholdValue: vector_float4](mpsimagehistogram/minpixelthresholdvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/zerohistogram)*