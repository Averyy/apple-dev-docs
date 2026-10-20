# histogramSize(forSourceFormat:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

The amount of space the histogram will take up in the output buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func histogramSize(forSourceFormat sourceFormat: MTLPixelFormat) -> Int
```

```objc
- (size_t) histogramSizeForSourceFormat:(MTLPixelFormat) sourceFormat;
```

#### Return Value

The number of bytes needed to store the histogram results.

#### Discussion

This convenience function calculates the minimum amount of space needed in the output histogram for the results. The buffer should be at least this length and longer if the `histogramOffset` value in the [`encode(to:sourceTexture:histogram:histogramOffset:)`](./encode%28to,sourcetexture,histogram,histogramoffset%29.md) method is non-zero.

## Parameters

- `sourceFormat`: The pixel format of the source image, corresponding to the `sourceTexture` object of the [`encode(to:sourceTexture:histogram:histogramOffset:)`](./encode%28to,sourcetexture,histogram,histogramoffset%29.md) method.

## See Also

### Methods
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](./init%28device,histograminfo%29.md)
  Initializes a histogram with specific information.
- [struct MPSImageHistogramInfo](../mpsimagehistograminfo.md)
  The information used to compute the histogram channels of an image.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](./encode%28to,sourcetexture,histogram,histogramoffset%29.md)
  Encodes the filter to a command buffer using a compute command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/histogramsize(forsourceformat:))*