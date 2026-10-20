# clipRectSource

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The source rectangle to use when reading data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var clipRectSource: MTLRegion { get set }
```

```objc
@property (nonatomic, readwrite) MTLRegion clipRectSource;
```

#### Discussion

This value indicates which part of the source image to read from. If the value of `clipRectSource` does not lie completely within the source image, then the intersection of the image bounds and the value of `clipRectSource` will be used. The value of `clipRectSource` replaces the [`offset`](../mpsunaryimagekernel/offset.md) value for this filter, which is ignored.

The default value is [`MPSRectNoClip`](../mpsrectnoclip.md), indicating that the entire source texture is used.

## See Also

### Properties
- [var zeroHistogram: Bool](./zerohistogram.md)
  Determines whether to zero-initialize the histogram results.
- [var histogramInfo: MPSImageHistogramInfo](./histograminfo.md)
  A structure describing the histogram content.
- [var minPixelThresholdValue: vector_float4](./minpixelthresholdvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/cliprectsource)*