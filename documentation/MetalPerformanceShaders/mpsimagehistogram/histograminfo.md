# histogramInfo

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

A structure describing the histogram content.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var histogramInfo: MPSImageHistogramInfo { get }
```

```objc
@property (nonatomic, readonly) MPSImageHistogramInfo histogramInfo;
```

#### Discussion

Returns a structure describing the format of the histogram.

## See Also

### Properties
- [var clipRectSource: MTLRegion](./cliprectsource.md)
  The source rectangle to use when reading data.
- [var zeroHistogram: Bool](./zerohistogram.md)
  Determines whether to zero-initialize the histogram results.
- [var minPixelThresholdValue: vector_float4](./minpixelthresholdvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/histograminfo)*