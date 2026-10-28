# zeroHistogram

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) BOOL zeroHistogram;
```

## Discussion

Determines whether the memory region in which the histogram results are to be written in the histogram buffer are to be zero-initialized or not.

The default value is [`true`](../../Swift/true.md).

## See Also

### Properties
- [var clipRectSource: MTLRegion](./cliprectsource.md)
  The source rectangle to use when reading data.
- [var histogramInfo: MPSImageHistogramInfo](./histograminfo.md)
  A structure describing the histogram content.
- [var minPixelThresholdValue: vector_float4](./minpixelthresholdvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/zerohistogram)*